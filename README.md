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