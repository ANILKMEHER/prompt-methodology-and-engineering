# Core Prompting Techniques, Analogies, & Templates 🛠️

This document outlines primary prompting methodologies, providing an operational analogy, structural template, and use-case criteria for each.

---

## 1. Zero-Shot Prompting
*   **What it is:** Asking the model to perform a task without providing any illustrative examples.
*   **The Analogy:** Handing an experienced developer a clear, standard ticket with no sample code files attached and expecting immediate execution based on core knowledge.
*   **When to Use / Who Needs It:** Best for straightforward data classification, general text summarization, or high-level brainstorming tasks.
*   **Strict Template:**
```text
    [Context]: You are an enterprise logging service.
    [Task]: Classify the incoming error message into one of these buckets: CRITICAL, WARNING, INFO.
    [Input]: "Database connection timed out after 3000ms."
    [Output Format]: JSON only.
    ```

---

## 2. Few-Shot Prompting
*   **What it is:** Providing the model with a small set of high-quality examples to establish expected pattern constraints before asking for the final output.
*   **The Analogy:** Providing a new hire with three completed pull requests to study before letting them commit code to the main codebase.
*   **When to Use / Who Needs It:** Critical when outputs must adhere to complex structures, custom language syntax, or nuanced corporate tones.
*   **Strict Template:**
```text
    [Task]: Convert user complaints into formal system incident descriptions.
    
    Example 1:
    User: "The screen went blank and I lost my unsaved data!"
    Incident: [Severity: High] UI rendering crash leading to uncommitted state loss.
    
    Example 2:
    User: "It takes forever to load the reports page."
    Incident: [Severity: Medium] Performance degradation identified on reporting endpoint.
    
    User: "I can't log in using my mobile token."
    Incident: [Severity: High] Authentication failure identified on mobile credential validation pathway.
    ```

---

## 3. Chain-of-Thought (CoT) Prompting
*   **What it is:** Forcing the model to explicitly output its intermediate logical reasoning steps before presenting the final answer.

<Image src="image_agent_tag_11678686885724967145" alt="Infographic illustrating the step-by-step nature of Chain of Thought prompting" caption="Chain of Thought Step Escalation" />

*   **The Analogy:** A math instructor requiring students to write out every line of an algebraic derivation on their exam sheets rather than just writing down the final value.
*   **When to Use / Who Needs It:** Essential for deep analytical reasoning, logic validation, financial calculations, and auditing tasks.
*   **Strict Template:**
```text
    [Task]: Calculate total project refactoring effort.
    [Constraint]: Work step-by-step, outlining your mathematical logic before stating the final total hours.
    [Data]: We have 3 legacy systems. System A has 1200 lines of custom code. System B has 450 lines. System C has 3100 lines. The migration rate baseline is 4 hours per 100 lines.
    ```
