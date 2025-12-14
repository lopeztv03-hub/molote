# Terms & Privacy Hosting Guide

This folder includes:
- `terms_of_service.html`
- `privacy_policy.html`
- `HOST_TERMS.bat` (local hosting)

## Option A: Quick Local Host (for testing)
1. Double-click `HOST_TERMS.bat`
2. Open: http://localhost:8080/terms_of_service.html
3. You will need a public URL for TikTok verification; local URLs usually are not accepted.

## Option B: GitHub Pages (recommended)
1. Create a public repo (e.g., `tiktok-legal`)
2. Add these files; rename `terms_of_service.html` to `index.html`
3. Push to GitHub
4. Enable GitHub Pages:
   - Repo Settings → Pages → Source: Deploy from a branch → `main`
5. Your URL will be:
   - https://<your-username>.github.io/tiktok-legal/
6. Use that URL in TikTok Dashboard as the **Terms of Service URL**

## Option C: Netlify or Vercel
- Drag-and-deploy these files to Netlify or deploy a project on Vercel.
- Use the site URL provided (e.g., `https://your-site.netlify.app/`).

## Notes
- TikTok may require a publicly accessible HTTPS URL.
- GitHub Pages and Netlify URLs are generally accepted without extra verification.
