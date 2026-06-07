# LearnCraft AI - Test Cases v1

## Purpose

This document defines evaluation scenarios for LearnCraft AI v1. The test cases validate scope detection, file handling, mode behavior, output type behavior, learning objective awareness, contextual prerequisite injection, and final output quality.

Each test case should be evaluated against these baseline rules:

- No generic summaries.
- No chat-style clarification.
- Guided narrowing must happen through Step 3 selection options.
- Prerequisites must be contextual, brief, and explained once.
- Output must match selected mode, output type, learning objective, and accepted scope.

---

## Test Case Matrix

| ID | Coverage Area | Mode | Output Type | Learning Objective |
| --- | --- | --- | --- | --- |
| TC-01 | Broad topic | Study Guide | Solid Understanding | Learn |
| TC-02 | Broad topic | Lecture-Ready Presentation Pack | Full Presentation Pack | Teach |
| TC-03 | Broad topic | Focused Deep Dive | Just One Topic | Explore |
| TC-04 | Narrow topic | Study Guide | Quick Learning | Learn |
| TC-05 | Narrow topic | Focused Deep Dive | Advanced Concept Brief | Explore |
| TC-06 | Narrow topic | Lecture-Ready Presentation Pack | Slides + Speaker Notes | Teach |
| TC-07 | Ambiguous topic | Study Guide | Solid Understanding | Learn |
| TC-08 | Ambiguous topic | Focused Deep Dive | Study Guide | Explore |
| TC-09 | Ambiguous topic | Lecture-Ready Presentation Pack | Slides Only | Teach |
| TC-10 | Multiple subtopics | Study Guide | Deep Learning | Learn |
| TC-11 | Topic + File | Study Guide | Implementation Ready | Implement |
| TC-12 | Topic + File | Lecture-Ready Presentation Pack | Full Presentation Pack | Teach |
| TC-13 | Topic + File conflict | Focused Deep Dive | Just One Topic | Explore |
| TC-14 | File only | Study Guide | Solid Understanding | Learn |
| TC-15 | File only | Study Guide | Implementation Ready | Implement |
| TC-16 | File only | Lecture-Ready Presentation Pack | Slides + Speaker Notes | Teach |
| TC-17 | Lecture mode | Lecture-Ready Presentation Pack | Slides Only | Teach |
| TC-18 | Lecture mode | Lecture-Ready Presentation Pack | Full Presentation Pack | Teach |
| TC-19 | Study mode | Study Guide | Quick Learning | Interview |
| TC-20 | Study mode | Study Guide | Deep Learning | Learn |
| TC-21 | Deep Dive mode | Focused Deep Dive | Just One Topic | Explore |
| TC-22 | Deep Dive mode | Focused Deep Dive | Lecture Style | Teach |
| TC-23 | Implementation Ready | Study Guide | Implementation Ready | Implement |
| TC-24 | Implementation Ready | Study Guide | Implementation Ready | Learn |
| TC-25 | Interview objective | Study Guide | Solid Understanding | Interview |
| TC-26 | Interview objective | Focused Deep Dive | Advanced Concept Brief | Interview |
| TC-27 | Contextual prerequisites | Study Guide | Deep Learning | Learn |
| TC-28 | Just One Topic | Focused Deep Dive | Just One Topic | Explore |
| TC-29 | File concept ranking | Study Guide | Solid Understanding | Learn |
| TC-30 | Quality validation | Lecture-Ready Presentation Pack | Full Presentation Pack | Teach |

---

## Detailed Test Cases

### TC-01: Broad Topic Study Guide

| Field | Definition |
| --- | --- |
| Input | Mode: Study Guide; Topic: Machine Learning; File: None; Output Type: Solid Understanding; Learning Objective: Learn |
| Expected behavior | Do not generate immediately. Detect that the topic is too broad and provide guided narrowing options in Step 3. |
| Expected scope handling | Offer narrower scopes such as supervised learning basics, model training workflow, or machine learning fundamentals. |
| Expected output characteristics | After scope selection, produce structured learner-facing content with definitions, explanations, examples, key insights, and minimal prerequisites. |

### TC-02: Broad Topic Lecture Pack

| Field | Definition |
| --- | --- |
| Input | Mode: Lecture-Ready Presentation Pack; Topic: Cloud Computing; File: None; Output Type: Full Presentation Pack; Learning Objective: Teach |
| Expected behavior | Detect broad scope and ask the user to choose a teachable scope inside Step 3. |
| Expected scope handling | Recommend lecture-ready scopes such as cloud service models, cloud deployment models, or cloud migration basics. |
| Expected output characteristics | Generate slides, speaker notes, learning objectives, section flow, examples, recap, and suggested activities. |

### TC-03: Broad Topic Deep Dive

| Field | Definition |
| --- | --- |
| Input | Mode: Focused Deep Dive; Topic: Artificial Intelligence; File: None; Output Type: Just One Topic; Learning Objective: Explore |
| Expected behavior | Detect that the topic is too broad for Just One Topic. |
| Expected scope handling | Require selection of a narrow AI topic before generation, such as transformer attention or model evaluation. |
| Expected output characteristics | After narrowing, focus exclusively on the selected topic with depth over breadth and no broad AI overview. |

### TC-04: Narrow Topic Quick Learning

| Field | Definition |
| --- | --- |
| Input | Mode: Study Guide; Topic: Gradient descent learning rate; File: None; Output Type: Quick Learning; Learning Objective: Learn |
| Expected behavior | Proceed directly to concept extraction because the topic is narrow. |
| Expected scope handling | No guided narrowing required. Keep adjacent concepts limited to what is required for understanding. |
| Expected output characteristics | Provide essential definition, concise explanation, example, key insight, and fast recall points. |

### TC-05: Narrow Topic Advanced Brief

| Field | Definition |
| --- | --- |
| Input | Mode: Focused Deep Dive; Topic: Idempotency in REST APIs; File: None; Output Type: Advanced Concept Brief; Learning Objective: Explore |
| Expected behavior | Accept scope and generate focused expert-level analysis. |
| Expected scope handling | No broad API overview. Include HTTP method behavior only where required. |
| Expected output characteristics | Include precise definitions, nuanced constraints, examples, implications, and key insight. |

### TC-06: Narrow Topic Lecture Notes

| Field | Definition |
| --- | --- |
| Input | Mode: Lecture-Ready Presentation Pack; Topic: Binary search time complexity; File: None; Output Type: Slides + Speaker Notes; Learning Objective: Teach |
| Expected behavior | Proceed directly to lecture planning. |
| Expected scope handling | Keep scope to binary search complexity and required prerequisite explanation of logarithmic reduction. |
| Expected output characteristics | Generate slide titles, slide bullets, and speaker notes with teachable sequence and examples. |

### TC-07: Ambiguous Topic Java

| Field | Definition |
| --- | --- |
| Input | Mode: Study Guide; Topic: Java; File: None; Output Type: Solid Understanding; Learning Objective: Learn |
| Expected behavior | Detect ambiguity. |
| Expected scope handling | Show Step 3 interpretation choices such as Java programming language, JVM platform, or Java island. |
| Expected output characteristics | After selection, generate content only for the selected interpretation. |

### TC-08: Ambiguous Topic Spark

| Field | Definition |
| --- | --- |
| Input | Mode: Focused Deep Dive; Topic: Spark; File: None; Output Type: Study Guide; Learning Objective: Explore |
| Expected behavior | Detect ambiguity across Apache Spark, spark ignition, or brand/tool meanings. |
| Expected scope handling | Present selectable interpretations without open-ended questioning. |
| Expected output characteristics | Generate focused study material for the selected interpretation with no unrelated meanings. |

### TC-09: Ambiguous Topic Python

| Field | Definition |
| --- | --- |
| Input | Mode: Lecture-Ready Presentation Pack; Topic: Python; File: None; Output Type: Slides Only; Learning Objective: Teach |
| Expected behavior | Detect potential ambiguity but prioritize likely programming language interpretation as a selectable option. |
| Expected scope handling | If broad and ambiguous, show choices such as Python basics, Python data structures, Python for automation, or Python language. |
| Expected output characteristics | Generate concise slide content only after scope or interpretation is selected. |

### TC-10: Multiple Major Subtopics

| Field | Definition |
| --- | --- |
| Input | Mode: Study Guide; Topic: Neural networks, decision trees, and reinforcement learning; File: None; Output Type: Deep Learning; Learning Objective: Learn |
| Expected behavior | Detect multiple major subtopics. |
| Expected scope handling | Offer choices to focus on one subtopic, generate a structured sequence, or prioritize the most foundational topic first. |
| Expected output characteristics | If sequence is selected, order concepts logically and avoid treating all topics as a shallow list. |

### TC-11: Topic + File Implementation Ready

| Field | Definition |
| --- | --- |
| Input | Mode: Study Guide; Topic: Building a retrieval augmented generation pipeline; File: Architecture notes about vector search and embeddings; Output Type: Implementation Ready; Learning Objective: Implement |
| Expected behavior | Use the topic as intent and file as grounding material. |
| Expected scope handling | Prefer file sections directly related to vector search, chunking, embeddings, retrieval, and generation. |
| Expected output characteristics | Include practical workflow, setup requirements, real-world usage patterns, common mistakes, hands-on exercise, and next steps. |

### TC-12: Topic + File Lecture Pack

| Field | Definition |
| --- | --- |
| Input | Mode: Lecture-Ready Presentation Pack; Topic: OAuth 2.0 authorization code flow; File: Internal security training notes; Output Type: Full Presentation Pack; Learning Objective: Teach |
| Expected behavior | Align file concepts with the topic and create lecture-ready content. |
| Expected scope handling | Ignore unrelated security notes unless needed for brief context. |
| Expected output characteristics | Include slide flow, speaker notes, examples, recap, learning objectives, and activities. |

### TC-13: Topic + File Conflict

| Field | Definition |
| --- | --- |
| Input | Mode: Focused Deep Dive; Topic: Kubernetes deployments; File: Document primarily about Terraform modules; Output Type: Just One Topic; Learning Objective: Explore |
| Expected behavior | Detect topic and file conflict. |
| Expected scope handling | Show Step 3 alignment choices: use topic as primary focus, use file as primary focus, or use only file sections related to topic. |
| Expected output characteristics | After selection, preserve accepted scope and avoid broad DevOps overview. |

### TC-14: File Only Multi-Concept Study Guide

| Field | Definition |
| --- | --- |
| Input | Mode: Study Guide; Topic: None; File: Document covering supervised learning, model evaluation, and deployment; Output Type: Solid Understanding; Learning Objective: Learn |
| Expected behavior | Extract file concepts and structure. |
| Expected scope handling | Detect multiple concepts and show concept selection or sequence options in Step 3. |
| Expected output characteristics | Generate structured study material for selected concept or sequence, avoiding generic file summary. |

### TC-15: File Only Implementation Workflow

| Field | Definition |
| --- | --- |
| Input | Mode: Study Guide; Topic: None; File: Runbook for setting up CI/CD pipelines; Output Type: Implementation Ready; Learning Objective: Implement |
| Expected behavior | Extract procedures, setup steps, dependencies, and common operational patterns. |
| Expected scope handling | If multiple workflows exist, rank and suggest the most important workflow first. |
| Expected output characteristics | Include practical workflow, setup requirements, real-world usage patterns, common mistakes, exercise, and next steps. |

### TC-16: File Only Lecture Content

| Field | Definition |
| --- | --- |
| Input | Mode: Lecture-Ready Presentation Pack; Topic: None; File: Training manual on data privacy principles; Output Type: Slides + Speaker Notes; Learning Objective: Teach |
| Expected behavior | Extract sections and convert them into teachable presentation flow. |
| Expected scope handling | If file has multiple major sections, suggest sequence or focus options. |
| Expected output characteristics | Generate slides and notes with examples, section transitions, and concise learner-friendly explanations. |

### TC-17: Lecture Slides Only

| Field | Definition |
| --- | --- |
| Input | Mode: Lecture-Ready Presentation Pack; Topic: Event-driven architecture basics; File: None; Output Type: Slides Only; Learning Objective: Teach |
| Expected behavior | Generate slide-ready content without speaker notes. |
| Expected scope handling | Accept scope if limited to basics. |
| Expected output characteristics | Include slide titles, concise bullets, visual guidance, and teaching sequence. |

### TC-18: Full Presentation Pack

| Field | Definition |
| --- | --- |
| Input | Mode: Lecture-Ready Presentation Pack; Topic: Introduction to prompt engineering; File: None; Output Type: Full Presentation Pack; Learning Objective: Teach |
| Expected behavior | Build full teaching package. |
| Expected scope handling | If topic is broad, suggest narrower lecture scopes such as prompt structure, evaluation, or examples. |
| Expected output characteristics | Include slides, speaker notes, learning objectives, section flow, examples, recap, and suggested activities. |

### TC-19: Study Mode Interview Objective

| Field | Definition |
| --- | --- |
| Input | Mode: Study Guide; Topic: SQL joins; File: None; Output Type: Quick Learning; Learning Objective: Interview |
| Expected behavior | Generate interview-oriented quick learning content. |
| Expected scope handling | Scope is acceptable but should not expand into all SQL. |
| Expected output characteristics | Include high-frequency join concepts, concise examples, misconceptions, and likely interview questions. |

### TC-20: Study Mode Deep Learning

| Field | Definition |
| --- | --- |
| Input | Mode: Study Guide; Topic: Backpropagation intuition; File: None; Output Type: Deep Learning; Learning Objective: Learn |
| Expected behavior | Generate deep learner-facing explanation. |
| Expected scope handling | Include only required prerequisites such as gradients and chain rule, briefly and contextually. |
| Expected output characteristics | Include layered explanations, examples, misconceptions, edge cases, and key insights. |

### TC-21: Deep Dive Just One Topic

| Field | Definition |
| --- | --- |
| Input | Mode: Focused Deep Dive; Topic: Transformer self-attention; File: None; Output Type: Just One Topic; Learning Objective: Explore |
| Expected behavior | Focus only on self-attention. |
| Expected scope handling | Avoid broad transformer architecture overview unless a brief contextual bridge is needed. |
| Expected output characteristics | Provide deep conceptual treatment, minimal prerequisites, examples, and key insight. |

### TC-22: Deep Dive Lecture Style

| Field | Definition |
| --- | --- |
| Input | Mode: Focused Deep Dive; Topic: CAP theorem tradeoffs; File: None; Output Type: Lecture Style; Learning Objective: Teach |
| Expected behavior | Generate focused lecture-style explanation. |
| Expected scope handling | Keep content on CAP theorem and required distributed systems context. |
| Expected output characteristics | Include teachable sequence, examples, misconceptions, recap, and audience-ready framing. |

### TC-23: Implementation Ready Implement Objective

| Field | Definition |
| --- | --- |
| Input | Mode: Study Guide; Topic: Setting up a Dockerized FastAPI application; File: None; Output Type: Implementation Ready; Learning Objective: Implement |
| Expected behavior | Generate actionable implementation guide. |
| Expected scope handling | Keep scope to FastAPI Docker setup and avoid broad container theory. |
| Expected output characteristics | Include workflow, setup requirements, file structure guidance, usage patterns, common mistakes, exercise, and next steps. |

### TC-24: Implementation Ready Learn Objective

| Field | Definition |
| --- | --- |
| Input | Mode: Study Guide; Topic: Git branching workflow; File: None; Output Type: Implementation Ready; Learning Objective: Learn |
| Expected behavior | Blend practical workflow with learner-friendly explanations. |
| Expected scope handling | Avoid expanding into all Git internals. |
| Expected output characteristics | Include implementation sections plus definitions, explanation, example, key insight, and recommended next steps. |

### TC-25: Interview Objective Study Guide

| Field | Definition |
| --- | --- |
| Input | Mode: Study Guide; Topic: Object-oriented programming principles; File: None; Output Type: Solid Understanding; Learning Objective: Interview |
| Expected behavior | Generate interview-focused study material. |
| Expected scope handling | If broad, suggest focusing on SOLID, inheritance vs composition, encapsulation, or polymorphism. |
| Expected output characteristics | Include high-frequency concepts, misconceptions, concise examples, and likely interview questions. |

### TC-26: Interview Objective Deep Dive

| Field | Definition |
| --- | --- |
| Input | Mode: Focused Deep Dive; Topic: Database indexing tradeoffs; File: None; Output Type: Advanced Concept Brief; Learning Objective: Interview |
| Expected behavior | Generate focused advanced brief for interview preparation. |
| Expected scope handling | Keep scope to indexing tradeoffs and avoid full database architecture overview. |
| Expected output characteristics | Include tradeoffs, common misconceptions, practical examples, and likely interview questions. |

### TC-27: Contextual Prerequisites

| Field | Definition |
| --- | --- |
| Input | Mode: Study Guide; Topic: Bayesian inference; File: None; Output Type: Deep Learning; Learning Objective: Learn |
| Expected behavior | Identify required prerequisites such as prior, likelihood, and posterior. |
| Expected scope handling | Do not create a prerequisite chapter on probability theory. |
| Expected output characteristics | Explain prerequisites briefly when first needed, explain once, and continue with the main topic. |

### TC-28: Just One Topic Scope Discipline

| Field | Definition |
| --- | --- |
| Input | Mode: Focused Deep Dive; Topic: Cache invalidation; File: None; Output Type: Just One Topic; Learning Objective: Explore |
| Expected behavior | Generate deep content on cache invalidation only. |
| Expected scope handling | Do not expand into broad caching architectures unless required for understanding. |
| Expected output characteristics | Optimize for depth, include examples and key insights, and keep prerequisites minimal. |

### TC-29: File Concept Ranking

| Field | Definition |
| --- | --- |
| Input | Mode: Study Guide; Topic: Model evaluation; File: Document covering data preprocessing, training, evaluation metrics, deployment, and monitoring; Output Type: Solid Understanding; Learning Objective: Learn |
| Expected behavior | Rank extracted file concepts using relevance, frequency, importance, and dependency relationships. |
| Expected scope handling | Suggest evaluation metrics and validation concepts before unrelated deployment or monitoring topics. |
| Expected output characteristics | Generate content grounded in relevant file sections and avoid generic document summary. |

### TC-30: Quality Validation Full Pack

| Field | Definition |
| --- | --- |
| Input | Mode: Lecture-Ready Presentation Pack; Topic: Agile sprint planning; File: None; Output Type: Full Presentation Pack; Learning Objective: Teach |
| Expected behavior | Generate only after internal validation passes. |
| Expected scope handling | Keep scope to sprint planning, not all Agile methodology. |
| Expected output characteristics | Must not be a generic summary; must include slides, notes, objectives, flow, examples, recap, activities, and no repeated prerequisites. |

