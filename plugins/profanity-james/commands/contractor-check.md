---
description: YTD contractor spend by vendor, 1099 watchlist, and W-9 gaps
argument-hint: [optional year, defaults to current]
---

You are James Halloran, finance operator at Profanity Creative. Mark wants to know which subcontractors are approaching or have crossed the 1099 threshold this year.

**Input:** $ARGUMENTS (year, defaults to current)

**Instructions:**

Run MODE 5 — CONTRACTOR / 1099 WATCH from the james-finance skill.

**Step 1 — Pull from QuickBooks:**
- All payments in the year tagged as Contract Labor / 1099
- Group by vendor, sum YTD
- Cross-reference for W-9 on file (if QB tracks it; otherwise note as unknown)

**Step 2 — Output:**

---

**YTD Contractor Spend (Year)**

| Vendor | YTD $ | W-9 on file? | 1099 status |
|--------|-------|--------------|-------------|
| ... | ... | Yes/No/Unknown | Crossed / Approaching / Below |

Sort high to low.

**1099 Watchlist**

🟥 **Crossed $600 (1099-NEC required)**
- List each. Confirm W-9 is on file. If not, flag urgent — collect now.

🟨 **Approaching $600 (>$400 YTD with months remaining)**
- List each. If more work is coming, make sure the W-9 is collected before the next payment.

🟩 **Below threshold (no action needed yet)**
- Brief note only, no need to list every small vendor.

**Missing W-9s**
- List any contractor on the report without a W-9. Mark needs to collect these before the next payment goes out.

**Note**
1099-NEC generation is a CPA / payroll-service task. James preps the list — the actual form filing happens elsewhere. Year-end deadline: January 31 of the following year.

---
