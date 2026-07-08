import re
import os

BASE = "/app/data/所有对话/主对话/uuyckz/com.cn"

# New 5-column footer HTML
new_footer = '''<footer class="footer">
<div class="container">
<div class="footer-grid">
  <div class="footer-col">
    <h4>产品</h4>
    <ul><li><a href="https://uuyckz.com.cn/download.html">下载中心</a></li><li><a href="https://uuyckz.com.cn/#features">功能特性</a></li><li><a href="https://uuyckz.com.cn/articles.html">技术文章</a></li><li><a href="https://uuyckz.com.cn/#faq">常见问题</a></li></ul>
  </div>
  <div class="footer-col">
    <h4>下载</h4>
    <ul><li><a href="https://uuyckz.com.cn/dl/uuyckz-setup-win.exe">Windows版下载</a></li><li><a href="https://uuyckz.com.cn/dl/uuyckz-setup-mac.dmg">macOS版下载</a></li><li><a href="https://uuyckz.com.cn/dl/uuyckz-ios.html">iOS版下载</a></li><li><a href="https://uuyckz.com.cn/dl/uuyckz-android.apk">Android版下载</a></li></ul>
  </div>
  <div class="footer-col">
    <h4>教程</h4>
    <ul><li><a href="https://uuyckz.com.cn/article-1.html">新手入门教程</a></li><li><a href="https://uuyckz.com.cn/article-3.html">远程办公设置</a></li><li><a href="https://uuyckz.com.cn/article-5.html">游戏串流优化</a></li><li><a href="https://uuyckz.com.cn/article-6.html">远程开机配置</a></li></ul>
  </div>
  <div class="footer-col">
    <h4>关于</h4>
    <ul><li><a href="https://uuyckz.com.cn/">关于UU远程</a></li><li><a href="https://uuyckz.com.cn/articles.html">更新日志</a></li><li><a href="https://uuyckz.com.cn/article-4.html">安全说明</a></li><li><a href="mailto:support@uuyckz.com.cn">联系我们</a></li></ul>
  </div>
  <div class="footer-col">
    <h4>法律</h4>
    <ul><li><a href="https://uuyckz.com.cn/privacy-policy.html">隐私政策</a></li><li><a href="https://uuyckz.com.cn/terms-of-service.html">用户协议</a></li><li><a href="https://uuyckz.com.cn/cookie-policy.html">Cookie政策</a></li></ul>
  </div>
</div>
<div class="footer-bottom"><p>&copy; 2025 广州网易计算机系统有限公司 版权所有 | UU远程控制</p></div>
</div>
</footer>'''

# Footer CSS to add
footer_css = '''
.footer{background:#0a1628;border-top:1px solid rgba(0,214,143,0.08);padding:2.5rem 0 1rem;margin-top:3rem}
.footer-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:2rem;margin-bottom:2rem}
.footer-col h4{color:#00d68f;font-size:0.95rem;font-weight:700;margin-bottom:0.8rem;letter-spacing:0.02em}
.footer-col ul{list-style:none;padding:0}
.footer-col ul li{margin-bottom:0.5rem}
.footer-col ul li a{color:#8899aa;font-size:0.85rem;transition:color .3s}
.footer-col ul li a:hover{color:#00d68f}
.footer-bottom{border-top:1px solid rgba(0,214,143,0.08);padding-top:1rem;text-align:center}
.footer-bottom p{color:#8899aa;font-size:0.82rem}
@media(max-width:768px){.footer-grid{grid-template-columns:repeat(2,1fr);gap:1.5rem}}
@media(max-width:480px){.footer-grid{grid-template-columns:1fr}}
'''

# Files to update
files = [f'article-{i}.html' for i in range(1, 11)] + ['download.html', 'articles.html']

for filename in files:
    filepath = os.path.join(BASE, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace old footer with new footer
    old_footer_pattern = r'<footer class="footer">.*?</footer>'
    content = re.sub(old_footer_pattern, new_footer, content, flags=re.DOTALL)
    
    # 2. Replace old footer CSS with new footer CSS
    # Remove old footer CSS line
    old_footer_css_pattern = r'\.footer\{background:#0d1a2e;border-top:1px solid rgba\(0,214,143,0\.08\);padding:2rem 0 1rem;margin-top:3rem;text-align:center\}\.footer p\{color:#8899aa;font-size:0\.82rem\}'
    content = re.sub(old_footer_css_pattern, footer_css, content)
    
    # Also handle article-7's variant footer CSS (it may have slightly different format)
    old_footer_css2 = r'\.footer\{background:#0d1a2e;border-top:1px solid rgba\(0,214,143,0\.08\);padding:2rem 0 1rem;margin-top:3rem;text-align:center\}\.footer p\{color:#8899aa;font-size:0\.82rem\}'
    content = re.sub(old_footer_css2, footer_css, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated footer in {filename}")

print("\nAll footers updated!")
