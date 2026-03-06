# Clara AI Agent Automation Pipeline

## Overview

This project builds an automation pipeline that converts demo and onboarding call transcripts into structured AI voice agent configurations.

The system extracts operational rules from transcripts and generates versioned agent specifications.

## Architecture

Demo Transcript
↓
Extraction Script
↓
Account Memo JSON (v1)
↓
Agent Spec Generator

Onboarding Transcript
↓
Update Script
↓
Account Memo JSON (v2)
↓
Agent Spec Generator
↓
Changelog showing differences

## Setup

Create environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

## Run Pipeline

python run_pipeline.py

## Dataset

Place transcripts inside:

dataset/demo_calls
dataset/onboarding_calls

## Output

Generated outputs are stored in:

outputs/accounts/<account_id>

Each account contains:

v1
- account_memo.json
- agent_spec.json

v2
- account_memo.json
- agent_spec.json
- changes.md

## Limitations

Extraction is rule-based and does not use an LLM.

## Future Improvements

- LLM-based extraction
- Retell API integration
- Web dashboard


## Repository Structure

```
automation-pipeline-assignment
│
├── dataset
│   ├── demo_calls
│   │   └── demo1.txt
│   └── onboarding_calls
│       └── onboard1.txt
│
├── scripts
│   ├── extract_demo_data.py
│   ├── generate_agent_spec.py
│   ├── onboarding_update.py
│   ├── changelog.py
│   └── utils.py
│
├── outputs
│   └── accounts
│       └── acc_<account_id>
│           ├── v1
│           │   ├── account_memo.json
│           │   └── agent_spec.json
│           │
│           └── v2
│               ├── account_memo.json
│               ├── agent_spec.json
│               └── changes.md
│
├── workflows
│   └── pipeline_workflow.md
│
├── logs
│   └── pipeline.log
│
├── run_pipeline.py
├── requirements.txt
└── README.md
```

This structure shows how transcripts are processed into versioned agent configurations.