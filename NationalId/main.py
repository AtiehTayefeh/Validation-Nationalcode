from fastapi import FastAPI
import uvicorn

app = FastAPI()

def is_valid_iranian_national_id(national_id: str) -> bool:
    if not national_id.isdigit() or len(national_id) != 10:
        return False

    codemelli = [int(d) for d in national_id]
    s = sum(codemelli[i] * (10 - i) for i in range(9))
    remainder = s % 11
    check_digit = (11 - remainder) % 10

    return codemelli[9] == check_digit

@app.get("/validate_national_id/")
async def validate_national_id(national_id: str):
    is_valid = is_valid_iranian_national_id(national_id)
    if is_valid:
        return {"national_id": national_id, "is_valid": True, "message": "کد ملی معتبر است."}
    else:
        return {"national_id": national_id, "is_valid": False, "message": "کد ملی نامعتبر است."}

# برای اجرای این API، باید این کد را در یک فایل پایتون (مثلاً main.py) ذخیره کنید
# و سپس در ترمینال دستور زیر را اجرا کنید:
# uvicorn main:app --reload
# پس از آن می‌توانید از طریق مرورگر یا ابزارهایی مانند curl یا Postman به آدرس
# http://127.0.0.1:8000/validate_national_id/?national_id=2093664402
# درخواست ارسال کنید.

# توجه: اجرای مستقیم uvicorn در این محیط امکان‌پذیر نیست.
# کد بالا ساختار API را نشان می‌دهد و باید در محیط توسعه شما اجرا شود.
