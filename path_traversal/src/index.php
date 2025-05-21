<?php
$imageDir = './file/';  // 圖片資料夾的路徑
$images = glob($imageDir . '*.{jpg,jpeg,png,gif}', GLOB_BRACE);
?>

<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>貓咪相簿</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .card {
            border: none;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .card-body {
            padding: 2rem;
        }
        h1 {
            color: #343a40;
            font-weight: bold;
        }
        .img-hover-zoom {
            overflow: hidden;
            border-radius: 10px;
        }
        .img-hover-zoom img {
            transition: transform .5s ease;
            width: 100%;
            height: auto;
        }
        .img-hover-zoom:hover img {
            transform: scale(1.05);
        }
        .btn-floating {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            text-align: center;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
            z-index: 1000;
        }
        .grid-item {
            width: 100%;
            padding: 10px;
        }
        @media (min-width: 576px) {
            .grid-item {
                width: 50%;
            }
        }
        @media (min-width: 992px) {
            .grid-item {
                width: 33.333%;
            }
        }
    </style>
</head>
<body>
    <div class="container py-5">
        <div class="card mb-4">
            <div class="card-body text-center">
                <h1 class="display-4 mb-3">🐱 貓咪相簿 🐱</h1>
                <p class="lead text-muted">探索我們可愛的貓咪照片集！點擊圖片可在新分頁中查看原圖。</p>
            </div>
        </div>

        <div class="grid">
            <?php foreach ($images as $image): ?>
            <?php $filename = basename($image); ?>
            <div class="grid-item">
                <div class="card img-hover-zoom">
                    <a href="load.php?file=<?php echo urlencode($filename); ?>" target="_blank">
                        <img src="load.php?file=<?php echo urlencode($filename); ?>" class="card-img-top" alt="貓咪圖片">
                    </a>
                </div>
            </div>
            <?php endforeach; ?>
        </div>
    </div>

    <a href="#" class="btn btn-primary btn-floating">
        <i class="fas fa-arrow-up"></i>
    </a>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://unpkg.com/masonry-layout@4/dist/masonry.pkgd.min.js"></script>
    <script src="https://unpkg.com/imagesloaded@5/imagesloaded.pkgd.min.js"></script>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        var grid = document.querySelector('.grid');
        var msnry;

        imagesLoaded(grid, function() {
            msnry = new Masonry(grid, {
                itemSelector: '.grid-item',
                columnWidth: '.grid-item',
                percentPosition: true
            });
        });
    });
    </script>
</body>
</html>