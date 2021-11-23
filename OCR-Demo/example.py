import ocrspace



api = ocrspace.API()
TEST_IMAGE_URL = 'https://i.redd.it/4z5kc6qwo8f51.jpg'

print('Testing URL-based OCR:')
print(api.ocr_url(TEST_IMAGE_URL))




print('Testing file-based OCR:')

TEST_FILENAME = 'Test.jpg'
print(api.ocr_file(TEST_FILENAME))


