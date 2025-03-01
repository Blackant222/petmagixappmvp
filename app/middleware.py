# Last modified: 2025-03-01 12:22:16 by Blackant222
from fastapi import Request
from datetime import datetime
import time

async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["X-Modified-By"] = "Blackant222"
    response.headers["X-Modified-At"] = "2025-03-01 12:22:16"
    return response