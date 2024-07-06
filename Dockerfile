FROM --platform=linux/amd64 python:3.8
# tạo thư mục trong container
WORKDIR /app

# Copy tất cả các file vào container /app
COPY . /app

# Cho phép chỉnh sửa file trong thư mục /app
RUN chmod 0744 /app
# 
# RUN pip install --no-cache-dir --upgrade -r requirements.txt 
RUN pip install -r requirements.txt 

# Nếu không dùng supervisord thì bật đoạn này lên
# CMD ["python", "cron_init.py"]

# Cài đặt supervisor
RUN apt-get update && apt-get install -y supervisor

# Tạo thư mục cho các file cấu hình của supervisor
RUN mkdir -p /etc/supervisor/conf.d

# Copy file cấu hình supervisor vào container
COPY supervisord.conf /etc/supervisor/supervisord.conf

# Khởi động supervisor
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]