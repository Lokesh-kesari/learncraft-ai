# LearnCraft AI - Product Specification v1

## Vision

LearnCraft AI transforms topics and documents into structured learning experiences tailored to a user's objective, rather than generating generic explanations or summaries.

The platform helps users learn, teach, implement, and deeply explore concepts through a guided 3-step workflow.

---

## Problem Statement

Generative AI can explain almost any topic, but users still face challenges:

* Information is often unstructured.
* Users may not know prerequisite concepts.
* Learning material is rarely tailored to the user's goal.
* Teaching material requires significant manual preparation.
* Deep exploration of a concept often includes unnecessary information.

LearnCraft AI addresses these challenges by adapting content generation to the user's learning intent.

---

## Target Users

### Primary Users

* Students
* Professionals
* Engineers
* Trainers
* Interview candidates

### Secondary Users

* Educators
* Content creators
* Corporate trainers

---

## Core Value Proposition

Transform a topic or document into a learning experience optimized for a specific objective.

---

## User Flow

### Step 1: Select Mode

Options:

* Lecture-Ready Presentation Pack
* Study Guide
* Focused Deep Dive

---

### Step 2: Provide Input

User can provide:

* Topic
* File Upload
* Topic + File

Validation:

At least one input is required.

---

### Step 3: Select Output

#### Lecture Mode

* Slides Only
* Slides + Speaker Notes
* Full Presentation Pack

#### Study Guide

* Quick Learning
* Solid Understanding
* Deep Learning
* Implementation Ready

#### Focused Deep Dive

* Lecture Style
* Study Guide
* Advanced Concept Brief
* Just One Topic

---

## Learning Objective

The system may adapt outputs based on the user's objective:

* Learn
* Teach
* Implement
* Explore

---

## Key Differentiator

### Contextual Prerequisite Injection

Instead of generating prerequisite chapters, LearnCraft AI injects prerequisite explanations only when they become necessary.

Rules:

* Keep explanations brief.
* Explain only the required knowledge.
* Do not repeat prerequisite explanations.
* Integrate naturally into the learning flow.

---

## Topic Scope Detection

If a topic is too broad:

Example:

Machine Learning

The system should require the user to narrow the scope through guided selection before generation.

---

## Output Structure

Each concept should include:

1. Definition
2. Explanation
3. Example
4. Key Insight

Additional content may vary based on mode.

---

## Constraints

* Maximum 3-step workflow
* Selection-driven navigation
* No chat-style questioning
* No repetitive clarification requests
* No generic summaries
* Content must match user intent

---

## Success Criteria

* User completes workflow in 3 steps or fewer
* Generated content is immediately usable
* Minimal editing required
* Learning experience feels tailored to the objective
* Prerequisites improve understanding without creating unnecessary content

---

## Version

v1.0 Planning Phase
