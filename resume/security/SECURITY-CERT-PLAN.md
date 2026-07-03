# Security & Concierge — Cert Renewal + Apply Strategy

**Honest rule:** Do not claim CPR, WHMIS, or Security Licence as "valid" on applications until they are. Your updated resume says **renewal in progress** and **completing before start date** — that is accurate if you book renewals this week.

---

## This week: renew before heavy security applying (1–3 days total)

| Cert | Where | Time | Cost (approx.) |
|------|-------|------|----------------|
| **WHMIS** | [Ontario WHMIS online](https://www.ontario.ca/page/workplace-hazardous-materials-information-system-whmis) or St John / employer-approved provider | 1–2 hours | $20–40 |
| **First Aid + CPR (Level C)** | St John Ambulance Brampton/Mississauga or Canadian Red Cross | 1 day course | $80–120 |
| **Security Guard Licence** | ServiceOntario + approved training provider if lapsed | Varies | Check renewal status at ServiceOntario |

After each cert: update `profile.yml` → `certifications` and re-run `..\..\resumes\compile_all.ps1`.

---

## Which jobs to target right now

| Job requirement | Your status | Strategy |
|-----------------|-------------|----------|
| Security Licence (required) | Renewal in progress | Apply + state completion date in cover letter |
| CPR / First Aid (preferred or required) | Lapsed — renew this week | Book course; put date in email: "CPR recertification scheduled [date]" |
| WHMIS | Lapsed | Complete online before next security apply batch |
| Concierge 1 year (required) | No formal concierge title | Lead with **6 years customer service** (Fiverr) + venue/community front-line — see resume |
| Customer service 1 year | ✅ 6+ years | Strong match |
| Post-secondary education | ✅ Laurier BA in progress | Exceeds secondary school requirement |
| MS Office / Excel | ✅ | Listed on resume |
| Driver's licence (preferred) | ✅ **G2 valid** (full G pending) | List **G2** on forms — meets most patrol/concierge commute needs; do not claim full G until passed |

**ATS note:** Some postings auto-reject without "Concierge" in title. Apply anyway on email/Indeed where a human reads; for strict ATS portals, prioritize "Security Guard" / "Mobile Patrol" / "Customer Service" titles until CPR + licence are current.

---

## Regenerate security packets after resume update

```powershell
cd tools\apply-pipeline
..\..\resumes\compile_all.ps1          # rebuild resume_security.pdf (needs pdflatex)
.\run.ps1 regenerate --date 2026-06-22   # refresh cover letters (security folders)
```

Or single new application:
```powershell
.\run.ps1 create -c "Employer" -r "Corporate Concierge" -l "Brampton" `
  --variant security_ops --jd-file posting.txt
```

---

## Docker Desktop (not blocking job apps)

Install failed because **Windows Server service** is disabled. When you need Docker later:

1. `Win + R` → `services.msc`
2. Find **Server** → Startup type: **Manual** or **Automatic** → Start
3. Retry Docker Desktop install

You do **not** need Docker to send applications today.

---

## Cover letter angle (concierge / security)

Use this block when CPR/licence are renewing:

> I am completing Ontario Security Guard Licence renewal, Standard First Aid/CPR Level C, and WHMIS recertification before my available start date. I bring six years of documented customer service (1,400+ rated client engagements), three years of live-venue operations at Laurier Athletics, and strong record-keeping and computer skills (Word, Excel, Gmail). I am professional, punctual, and comfortable in fast-paced, public-facing environments.

This is already woven into the overhauled `resume_security.tex`.
