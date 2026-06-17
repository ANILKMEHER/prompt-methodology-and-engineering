# Prompt Engineering Methodology Comparison Matrix 📊

This document provides a technical comparison of standard and advanced prompting methods, highlighting their operational trade-offs and token cost weights.

---

## ⚖️ Analytical Trade-Off Comparison

| Prompting Technique | Core Advantage | Primary Disadvantage | Relative Token Consumption Cost | Target Implementation Vector |
| :--- | :--- | :--- | :--- | :--- |
| **Zero-Shot** | Minimal prompt token overhead; maximum speed. | Higher risk of output formatting errors or hallucinations. | Low | Basic categorization and open text extraction pipelines. |
| **Few-Shot** | Drastically improves formatting adherence. | Increases prompt payload size, compounding costs over API batches. | Medium | Complex structural extractions (like text-to-JSON parsing). |
| **Chain-of-Thought** | Maximizes reasoning accuracy across math and logic tasks. | Output generation duration scales up, increasing latency and cost. | High | Deep root-cause analysis and automated financial calculations. |

---

## 💡 Architectural Guidance Notes

> **The Optimization Balance:** While advanced methods like Chain-of-Thought dramatically improve logic validation, they consume significantly more output tokens. In production systems, look to apply **Zero-Shot with strict JSON schemas** first to preserve latency, escalating to **Few-Shot** or **CoT** only when compliance metrics drop below target SLAs.
