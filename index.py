from flask import Flask, jsonify, render_template, request
from pathlib import Path

app = Flask(__name__, template_folder=".")
    'هادئ وعصري': 'استخدمي مساحات بيضاء وألوانًا طبيعية، واجعلي الشعار بسيطًا وسهل القراءة.',
    'فاخر': 'اختاري لونًا داكنًا مع لمسات ذهبية، واستخدمي خطًا أنيقًا ومساحات واسعة.',
    'مرح وشبابي': 'استخدمي ألوانًا حيوية وأشكالًا مرحة، مع شعار واضح يسهل تذكره.',
    'تقني': 'اعتمدي شبكة هندسية وأيقونات بسيطة، مع درجات الأزرق وتباين واضح.'
}

@app.get('/')
def home():
    return render_template('index.html')

@app.post('/recommend')
def recommend():
    data = request.get_json(silent=True) or {}
    theme = data.get('theme', '')
    return jsonify(recommendation=TIPS.get(theme, 'اختاري أسلوبًا مناسبًا لطبيعة مشروعك وجمهوره المستهدف.'))

if __name__ == '__main__':
    app.run(debug=True)
