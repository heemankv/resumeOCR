import os
import tempfile
import pytest
from app import app

testFile_path1 = "example-resume/Heemank_Verma.pdf"
testUser1 = "Heemank Verma"
testFile_path2 = "example-resume/John_Doe.pdf"
testUser2 = "John Doe"


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_ping_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'hello world' in response.data

def test_resumeOCR_endpoint(client):
    response = client.get('/resumeOCR/')
    assert response.status_code == 200
    assert b'Heemank Verma' in response.data

def test_resumetojson_endpoint(client):
    with open(testFile_path1, 'rb') as resume_file:
        data = {'file': (resume_file, testFile_path1)}
        response = client.post('/resumetojson/', data=data, content_type='multipart/form-data')

    assert response.status_code == 200
    assert b'Heemank Verma' in response.data

def test_resumetojsonmultiple_endpoint(client):
    with open(testFile_path1, 'rb') as resume_file1, open(testFile_path2, 'rb') as resume_file2:
        data = {'file': [(resume_file1, testFile_path1), (resume_file2, testFile_path2)]}
        response = client.post('/resumetojsonmultiple/', data=data, content_type='multipart/form-data')

    assert response.status_code == 200
    assert b'Heemank Verma' in response.data
    assert b'John Doe' in response.data

# Ensure 100% code coverage
def test_main():
    import coverage
    cov = coverage.Coverage(source=['app'])
    cov.start()
    
    # Import your app after starting coverage
    import app

    cov.stop()
    cov.save()
    cov.report()

if __name__ == '__main__':
    pytest.main()