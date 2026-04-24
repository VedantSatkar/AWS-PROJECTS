# 🚀 AWS Static Website Hosting using S3 + boto3

![AWS](https://img.shields.io/badge/AWS-S3-orange?style=for-the-badge\&logo=amazonaws)
![Python](https://img.shields.io/badge/Python-boto3-blue?style=for-the-badge\&logo=python)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen?style=for-the-badge)

---

## 📌 Project Overview

This project demonstrates how to **host a static website on AWS S3** and automate file uploads using **Python (boto3 SDK)**.

The website is fully deployed on AWS and publicly accessible via the S3 static website endpoint.

---

## 🎯 Objectives

* Host a static website using AWS S3
* Automate deployment using Python (boto3)
* Understand S3 permissions, policies, and hosting
* Learn real-world cloud deployment basics

---

## 🧰 Tech Stack

* ☁️ AWS S3
* 🐍 Python (boto3)
* 🌐 HTML + CSS

---

## 🏗️ Architecture

```
User → Browser → S3 Bucket → Static Website Hosting → HTML Page
```

---

## ⚙️ Implementation Steps

1. Created an S3 bucket (`vedant-static-site`)
2. Disabled block public access
3. Enabled static website hosting
4. Uploaded HTML file using boto3 script
5. Set correct metadata (`Content-Type: text/html`)
6. Configured bucket policy for public access
7. Accessed website via S3 endpoint

---

## 📂 Project Structure

```
project_5/
│
├── index.html
├── upload.py
├── screenshots/
│   ├── output_project_5.png
│   ├── output_2.png
│   ├── object_inside_bucket.png
│
└── README.md
```

---

## 💻 Key Code

### Python Script (Upload using boto3)

```python
import boto3

s3 = boto3.client('s3')

s3.upload_file(
    "index.html",
    "vedant-static-site",
    "index.html",
    ExtraArgs={
        "ContentType": "text/html",
        "ACL": "public-read"
    }
)

print("✅ Uploaded correctly with content-type!")
```

---

### HTML UI

Your website UI is styled using HTML + CSS
📄 Source: 

---

## 📸 Screenshots

### 🌐 Website Output

![Website](screenshots/output_project_5.png)

### 📦 S3 Bucket Objects

![Bucket](output_project .png)

---

## 💡 Key Learnings

* How S3 static hosting works
* Difference between Object URL vs Website Endpoint
* Importance of `Content-Type`
* AWS permissions & public access handling
* Automating AWS using boto3

---

## 🚀 Future Improvements

* Add custom domain using Route 53
* Enable HTTPS using CloudFront
* Add CI/CD pipeline for deployment

---

## 👨‍💻 Author

**Vedant Satkar**

📧 [vedantssatkar@gmail.com](mailto:vedantssatkar@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/vedant-satkar-731bb2298/)
💻 [GitHub](https://github.com/VedantSatkar)

---