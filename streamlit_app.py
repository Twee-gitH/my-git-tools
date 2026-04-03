import streamlit as st

# Setup the page appearance
st.set_page_config(page_title="MY GIT CHEATS", layout="centered")

st.title("📂 OFFICIAL GIT COMMANDS")

# The content for your viewers
git_content = """
# ==========================================
# 1. SAVE & PUSH (Update Live App)
# ==========================================
git add .
git commit -m "Update application"
git push origin main

# 2. SYNC & PULL (Get Web Changes)
# ==========================================
git pull origin main

# 3. UNDO & RESET (Fix Mistakes)
# ==========================================
# Reset everything to last save:
git reset --hard HEAD

# 4. STATUS & HISTORY (Check Work)
# ==========================================
git status
git log --oneline
"""

# Display the code block
st.code(git_content, language="bash")

st.success("✅ Content Loaded Successfully!")
