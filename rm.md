docker build --platform linux/amd64 -t khuong123/mtips5s_discord:dev_1 .
docker-compose up --build
<!-- docker build -t khuong123/mtips5s_web:dev_1 . -->
docker push khuong123/mtips5s_discord:dev_1

Học kỹ thêm hướng đối tượng
Để tối ưu hóa và tạo nhiều biến thể.

# Hoặc update
docker build --platform linux/amd64 -t khuong123/mtips5s_discord:dev_1 .
docker push khuong123/mtips5s_discord:dev_1


# Trên server
docker pull khuong123/mtips5s_discord:dev_1
docker compose up --remove-orphans --build -d


UPDATE image SET type = 'image' WHERE type = 'video' AND image_path LIKE '%.jpg';


docker exec -it wordpress sh



docker build -t my_flask_app .
docker run -d -p 5002:5000 my_flask_discord


docker-compose down
docker-compose up --build

