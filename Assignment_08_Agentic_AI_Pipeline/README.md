# Assignment 08 – Single Agent Pipeline

## Overview

This assignment was completed as part of the **Celebal Excellence Internship (CEI) 2026** under the **Data Science (DS001)** track at **Celebal Technologies**.

The objective of this assignment was to build a small **Single-Agent Smart Assistant** capable of understanding user queries, determining the appropriate type of request, routing the query to the corresponding tool, and returning a structured response.

The project demonstrates fundamental concepts of **Agentic AI**, including tool-based execution, conditional routing, error handling, logging, and interactive agent workflows.

---

## Problem Statement

**Build an Agentic AI Pipeline using a single-agent system.**

The implemented agent is designed to:

- Understand different types of user queries
- Determine the appropriate action using rule-based routing
- Call the relevant tool when required
- Handle general queries directly
- Return structured JSON-style responses
- Provide an interactive mode for user queries

---

## Agent Capabilities

The agent supports the following query types:

| Query Type | Handler |
|------------|---------|
| Mathematical calculations | Calculator Tool |
| Keyword extraction | Keyword Extraction Tool |
| Word counting | Word Count Tool |
| General queries | General Response Handler |

The routing logic checks the rules in sequence, and the **first matching rule determines the route**. Each tool performs a specific task, keeping the system modular and easy to extend.

---

## Agent Workflow

The basic workflow of the system is:

```text
User Query
    ↓
Query Analysis
    ↓
Conditional Routing
    ↓
┌──────────────┬──────────────────┬────────────────┬─────────────────┐
│              │                  │                │                 │
Calculator   Keywords         Word Count      General Response
│              │                  │                │
└──────────────┴──────────────────┴────────────────┴─────────────────┘
                         ↓
                  Structured Output
