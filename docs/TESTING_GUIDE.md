# 🧪 Agent Testing Guide

This guide provides comprehensive test scenarios for all agents in the Customer Experience Rescue Swarm project.

## 🚀 Getting Started

### Prerequisites
1. Ensure ADK Web is running: `adk web --port 8000`
2. Open browser to: http://localhost:8000
3. Select agent from dropdown
4. Copy and paste prompts below

### Testing Environment
- **Test Customer IDs**: C67890 (Gold Tier), C11111-C99999 (Various tiers)
- **Test Transcript IDs**: T12345 (Angry customer), T99999 (Happy customer)
- **Expected Tools**: Each agent has 3-7 tools available

---

## 🔍 Individual Agent Testing

### Triage Agent (`triage_agent`)
**Purpose**: Analyze customer sentiment and make escalation decisions

#### Test Prompt 1: High Priority Escalation
```
Analyze customer C67890 with transcript T12345 - they are extremely upset about a damaged product and threatening to leave.
```

#### Test Prompt 2: Low Priority Standard Process
```
Check customer C11111 with transcript T99999 - they have a simple billing question about their last invoice.
```

**Expected Behavior**: 
- ✅ Calls `CRM_LOOKUP_TOOL` and `TRANSCRIPT_RETRIEVAL_TOOL`
- ✅ Returns escalation decision with case file
- ✅ Considers customer tier and sentiment

---

### Solution Agent (`solution_agent`)
**Purpose**: Find optimal solutions based on policies and customer value

#### Test Prompt 1: High-Value Customer Issue
```
Find the best solution for customer C67890 who received a damaged laptop worth $1,200. They are a Gold tier customer with high lifetime value.
```

#### Test Prompt 2: Standard Customer Issue
```
What's the recommended solution for customer C22222 with a standard warranty claim on a $50 accessory?
```

**Expected Behavior**:
- ✅ Calls `POLICY_LOOKUP_TOOL` and `ORDER_STATUS_TOOL`
- ✅ Returns ranked solution options
- ✅ Considers customer tier in solution ranking

---

### Action Agent (`action_agent`)
**Purpose**: Execute solutions and communicate with customers

#### Test Prompt 1: Refund Processing
```
Execute actions for customer C67890: process a $1,200 refund for damaged laptop and send an apology email with expedited replacement offer.
```

#### Test Prompt 2: Communication Only
```
Send a follow-up communication to customer C33333 explaining the resolution steps for their billing inquiry.
```

**Expected Behavior**:
- ✅ Calls `REFUND_TOOL` and `SEND_COMMUNICATION_TOOL`
- ✅ Executes appropriate actions
- ✅ Provides confirmation of actions taken

---

## 🚀 Consolidated Agent Testing

### Customer Experience Rescue Swarm (`customer_experience_rescue_swarm`)
**Purpose**: Handle complete end-to-end customer issue workflow

#### Test Prompt 1: Angry High-Value Customer
```
Customer C67890 with transcript T12345 is complaining about a damaged item they received. They said "I will never buy from you again, this is the worst experience ever."
```

#### Test Prompt 2: Moderately Upset Customer
```
Handle customer C44444 with transcript T77777 who is upset about a late delivery but generally satisfied with product quality.
```

#### Test Prompt 3: Simple Inquiry
```
Process customer C55555 with transcript T88888 - they're asking about return policy for an item they haven't opened yet.
```

**Expected Behavior**:
- ✅ Uses all 6 tools: CRM, Transcript, Policy, Refund, Communication, plus workflow function
- ✅ Makes triage decision
- ✅ Finds appropriate solution
- ✅ Executes actions if escalation needed
- ✅ Provides complete resolution summary

---

## 🎼 Multi-Agent Orchestrator Testing

### Customer Rescue Orchestrator (`customer_rescue_orchestrator`)
**Purpose**: Coordinate multiple agents and provide detailed workflow logging

#### Test Prompt 1: Complex High-Priority Issue
```
Orchestrate a complete resolution for customer C67890 with transcript T12345. Customer is extremely angry about receiving a damaged expensive item.
```

#### Test Prompt 2: Multi-Issue Scenario
```
Coordinate between all agents to handle customer C66666 who has multiple issues: billing question, damaged item, and wants to upgrade their service.
```

**Expected Behavior**:
- ✅ Uses all 7 tools including orchestration function
- ✅ Provides detailed step-by-step workflow logging
- ✅ Demonstrates proper agent coordination
- ✅ Shows decision points and rationale

---

## 📈 Progressive Testing Scenarios

### Escalation Testing
Test agents with increasing complexity:

1. **Low Priority**:
   ```
   Customer C11111 has a simple question about their account balance
   ```

2. **Medium Priority**:
   ```
   Customer C22222 received wrong item but is understanding and patient
   ```

3. **High Priority**:
   ```
   Customer C33333 received damaged expensive item and is furious, demanding immediate action
   ```

### Sentiment Analysis Testing
Test different emotional states:

1. **Happy Customer**:
   ```
   Customer C12345 loves their purchase and wants to buy more items. They're praising your service.
   ```

2. **Neutral Customer**:
   ```
   Customer C23456 has a standard return request and is being polite and matter-of-fact.
   ```

3. **Frustrated Customer**:
   ```
   Customer C34567 is annoyed about shipping delays but willing to work with you on a solution.
   ```

4. **Angry Customer**:
   ```
   Customer C45678 is furious and demanding immediate refund, threatening to never shop again.
   ```

---

## 🔥 Edge Case Testing

### Complex Multi-Issue Scenarios

#### Test Prompt 1: VIP Crisis
```
Customer C99999 with transcript T11111 is a VIP Gold customer who received the wrong item, was charged twice, and the customer service agent was rude to them. They're threatening legal action and posting negative reviews on social media.
```

#### Test Prompt 2: Time-Sensitive Gift Issue
```
Handle customer C88888 who ordered a gift for their anniversary, it arrived broken, the replacement was also defective, and now the anniversary has passed. They're devastated and considering canceling their account.
```

#### Test Prompt 3: Repeat Offender
```
Customer C77777 has had three issues in the past month: late delivery, wrong item, and billing error. They're losing patience and considering switching to a competitor.
```

---

## 🛠️ Tool-Specific Testing

### Data Retrieval Testing
```
Look up all available information for customer C67890 including their tier status, lifetime value, recent order history, and communication preferences.
```

### Policy Testing
```
What are the company policies for handling damaged items for Gold tier customers versus Silver tier customers?
```

### Refund Processing Testing
```
Process different refund scenarios for customer C67890: partial refund, full refund, store credit, and expedited replacement options.
```

### Communication Testing
```
Draft appropriate communications for customer C67890: apology email, resolution confirmation, and follow-up satisfaction survey.
```

---

## 📋 Testing Checklist

### For Each Agent Test:
- [ ] Agent loads successfully in ADK Web
- [ ] All expected tools are available
- [ ] Agent responds appropriately to prompts
- [ ] Tool calls are made correctly
- [ ] Response quality is relevant and helpful
- [ ] Error handling works for edge cases

### Performance Monitoring:
- [ ] Check token usage in ADK Web interface
- [ ] Monitor execution time in trace view
- [ ] Verify tool execution logs
- [ ] Confirm no errors in console

### Functional Verification:
- [ ] **Triage decisions** are logical and consistent
- [ ] **Solution ranking** considers customer value
- [ ] **Action execution** confirms successful operations
- [ ] **Workflow coordination** shows proper agent handoffs
- [ ] **Communication tone** matches customer tier and sentiment

---

## 🎯 Recommended Testing Order

1. **Start Simple**: Begin with `triage_agent` using basic scenarios
2. **Add Complexity**: Test `solution_agent` with policy lookups
3. **Execute Actions**: Verify `action_agent` refund/communication flows
4. **End-to-End**: Test `customer_experience_rescue_swarm` complete workflows
5. **Full Coordination**: Finish with `customer_rescue_orchestrator` complex scenarios

---

## 📊 Expected Results Summary

| Agent | Tools | Key Functions | Expected Outputs |
|-------|-------|---------------|------------------|
| Triage | 3 | Sentiment analysis, escalation | Case file, escalation decision |
| Solution | 3 | Policy lookup, solution ranking | Ranked solution options |
| Action | 3 | Refund processing, communication | Action confirmations |
| Rescue Swarm | 6 | Complete workflow | End-to-end resolution |
| Orchestrator | 7 | Multi-agent coordination | Detailed workflow logs |

---

## 🆘 Troubleshooting

### Common Issues:
- **Agent not loading**: Check imports in agent.py files
- **Tool errors**: Verify shared_tools structure
- **No response**: Check ADK Web console for errors
- **Wrong behavior**: Review agent instructions and tool logic

### Quick Fixes:
```bash
# Restart ADK Web if needed
adk web --port 8000

# Test agent loading
python -c "from [agent_name].agent import root_agent; print(f'{root_agent.name} loaded')"
```

---

## 🎉 Success Indicators

You'll know your agents are working correctly when:
- ✅ All agents load without errors
- ✅ Tool calls execute successfully
- ✅ Responses are contextually appropriate
- ✅ Escalation logic works correctly
- ✅ Refunds and communications are processed
- ✅ Multi-agent coordination shows proper handoffs

**Happy Testing!** 🚀
