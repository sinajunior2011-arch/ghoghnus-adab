from flask import Flask, send_file, jsonify
import os

app = Flask(__name__)

# این تابع همه چیز رو خودش پیدا میکنه!
@app.route('/')
def home():
    return send_file('index.html')

@app.route('/<path:filename>')
def all_files(filename):
    try:
        return send_file(filename)
    except:
        return "صفحه پیدا نشد! اما نگران نباش 😊", 404

@app.route('/api/stats')
def stats():
    return jsonify({
        'students': 165,
        'teachers': 25,
        'exams': 52, 
        'results': 1340
    })

if __name__ == '__main__':
    print("🚀 سرور ققنوس ادب روشن شد!")
    print("🌐 همه صفحات آماده اند!")
    app.run(debug=True, port=5000)