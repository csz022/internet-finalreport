# fansinterface-report

這是一個使用 Django 建立的成員展示與互動專案，包含註冊、登入、驗證碼登入、成員列表、成員詳細頁，以及留言與圖片上傳功能。

## 功能

- 成員列表首頁
- 成員詳細頁
- 使用者註冊
- 使用者登入 / 登出
- 驗證碼登入
- 會員留言與圖片上傳

## 專案結構

```text
finalreport/
├── finalreport/        # Django 專案設定
├── mainsite/           # 主要 app
├── templates/          # HTML 模板
├── static/             # 靜態檔案
├── media/              # 使用者上傳檔案
├── manage.py
├── requirements.txt
└── README.md
```

## 環境需求

- Python 3.9 以上
- 建議使用虛擬環境 `venv`

## 安裝方式

如果你已經有虛擬環境：

```bash
cd /Users/chenshuzhen/workspace/finalreport
source ../VENV/bin/activate
pip install -r requirements.txt
```

如果你要重建虛擬環境：

```bash
cd /Users/chenshuzhen/workspace
python3 -m venv VENV
source VENV/bin/activate
cd finalreport
pip install -r requirements.txt
```

## 啟動專案

```bash
cd /Users/chenshuzhen/workspace/finalreport
source ../VENV/bin/activate
python manage.py migrate
python manage.py runserver
```

啟動後打開：

```text
http://127.0.0.1:8000/
```

## 主要路由

- `/`：成員列表
- `/member/<id>/`：成員詳細頁
- `/login/`：登入
- `/logout/`：登出
- `/register/`：註冊
- `/admin/`：Django 後台

## 常用指令

檢查專案設定：

```bash
python manage.py check
```

建立管理員：

```bash
python manage.py createsuperuser
```

產生 migration：

```bash
python manage.py makemigrations
python manage.py migrate
```

## 推到 GitHub

先在 GitHub 建立一個空的 repository，例如 `fansinterface-report`，不要先勾選 README、`.gitignore` 或 license。

然後在本機執行：

```bash
cd /Users/chenshuzhen/workspace/finalreport
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的帳號/fansinterface-report.git
git push -u origin main
```

## 注意事項

- `db.sqlite3` 是本機資料庫，已在 `.gitignore` 內。
- `media/` 是上傳資料夾，已在 `.gitignore` 內。
- 外層虛擬環境 `VENV/` 不應推到 GitHub。
