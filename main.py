from fastapi import FastAPI

app = FastAPI(title='fastapi-boilerplate-kr')

@app.get('/health')
def health():
    return {'status': 'ok'}
