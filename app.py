import streamlit as st
import streamlit.components.v1 as components

# 1. 设置页面配置 (标题和宽屏模式)
st.set_page_config(
    page_title="下班快乐",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. 读取 HTML 文件
with open("index.html", "r", encoding='utf-8') as f:
    html_code = f.read()

# 3. 注入 CSS 样式：隐藏 Streamlit 的默认菜单、页脚和内边距，实现全屏效果
st.markdown(
    """
    <style>
        /* 隐藏顶部的汉堡菜单和红线 */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}

        /* 隐藏底部的 "Made with Streamlit" */
        footer {visibility: hidden;}

        /* 移除页面默认的内边距，让 iframe 撑满屏幕 */
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            margin: 0;
        }

        /* 强制 iframe 全屏 */
        iframe {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            border: none;
            z-index: 99999; /* 保证在最上层 */
        }

        /* 隐藏滚动条 */
        ::-webkit-scrollbar {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 4. 渲染 HTML 组件
components.html(html_code, height=1000, scrolling=False)