# Agentic Customer Experience Rescue Swarm

A multi-agent system built with **Google Agent Development Kit (ADK)** that proactively handles customer issues based on sentiment analysis of call transcripts. Features **clean architecture** with **zero code duplication** and follows **ADK best practices**.

## 🎯 What This System Does

This intelligent customer service system automatically:
- **Analyzes** customer sentiment from call transcripts
- **Prioritizes** issues based on customer value and urgency  
- **Finds** optimal solutions using company policies
- **Executes** actions like refunds, replacements, or communications
- **Tracks** complete resolution workflows

**Result**: Proactive customer issue resolution that turns frustrated customers into loyal advocates.

## 🏗️ Architecture Overview

This project demonstrates **multiple agent patterns** you can use with ADK:

- **🔍 Individual Specialized Agents** - Triage, Solution, and Action agents that work independently
- **🎯 Consolidated Agent** - Single agent handling the complete workflow  
- **🚀 Multi-Agent Orchestrator** - Coordinates multiple agents working together
- **📦 Shared Tools Library** - Centralized, reusable tools eliminating code duplication

All agents use **shared tools** from a centralized library, ensuring **zero code duplication** and **easy maintenance**.

### **🔄 Complete System Architecture**

```
                    👤 USER REQUEST
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
   🔍 Individual     🎯 Consolidated   🚀 Orchestrator
     Agents           Agent             Pattern
        │                │                │
        ├─ triage_agent  │                ├─ Coordinates:
        ├─ solution_agent├─ Workflow:     │  ├─ Triage Phase
        └─ action_agent  │  ├─ Triage     │  ├─ Solution Phase
                         │  ├─ Solution   │  └─ Action Phase
                         │  └─ Action     │
                         │                │
        ┌────────────────┼────────────────┘
        │                │
        ▼                ▼
    📦 SHARED TOOLS LIBRARY
    ├── 🔧 CRM_LOOKUP_TOOL
    ├── 🔧 TRANSCRIPT_RETRIEVAL_TOOL  
    ├── 🔧 POLICY_LOOKUP_TOOL
    ├── 🔧 REFUND_TOOL
    └── 🔧 SEND_COMMUNICATION_TOOL
        │
        ▼
    ✅ CUSTOMER RESOLUTION
```

## 🤖 Available Agents

The system provides **5 different agents** to demonstrate various architectural patterns:

### **1. Individual Specialized Agents**

- **`triage_agent`** - Validates alerts and gathers customer context
  - Looks up customer details in CRM
  - Retrieves call transcripts
  - Decides on escalation based on customer value and issue severity

- **`solution_agent`** - Determines optimal resolution paths
  - Queries company policy knowledge base
  - Checks order status and inventory
  - Generates ranked list of potential solutions

- **`action_agent`** - Executes resolutions and communicates with customers
  - Processes refunds, re-shipments, or generates coupons
  - Sends personalized, empathetic communications
  - Logs incidents in CRM

### **2. Consolidated Agent**

- **`customer_experience_rescue_swarm`** - Complete workflow in single agent
  - Handles triage → solution → action workflow
  - Demonstrates consolidated agent pattern
  - Uses shared tools (no code duplication)

### **3. Multi-Agent Orchestrator**

- **`customer_rescue_orchestrator`** - Coordinates multiple agents
  - Orchestrates triage → solution → action workflow
  - Demonstrates proper multi-agent coordination
  - Shows detailed workflow logging and status tracking

## 🔧 Shared Tools Library

All agents use centralized tools from `shared_tools/`:

- **`CRM_LOOKUP_TOOL`** - Customer data lookup
- **`TRANSCRIPT_RETRIEVAL_TOOL`** - Call transcript retrieval
- **`POLICY_LOOKUP_TOOL`** - Company policy queries
- **`REFUND_TOOL`** - Process customer refunds
- **`SEND_COMMUNICATION_TOOL`** - Send customer communications

### **Benefits:**
- ✅ **Zero code duplication** - tools defined once, used everywhere
- ✅ **Easy maintenance** - update tool logic in one place
- ✅ **Consistent behavior** - all agents use same implementations
- ✅ **ADK compliance** - proper FunctionTool patterns

## 🔍 Key Features

- **🏗️ Clean Architecture** - Zero code duplication, proper separation of concerns
- **🔧 Shared Tools** - Centralized, reusable tool library
- **🎯 Multiple Patterns** - Individual, consolidated, and orchestrated agents
- **✅ ADK Compliance** - Proper FunctionTool patterns and agent discovery
- **🧪 Testable** - Individual tools and agents can be tested in isolation
- **📊 Observable** - Detailed logging and workflow tracking
- **🚀 Production Ready** - Follows best practices for maintainability

## 🚀 Getting Started

### **Prerequisites**
- Python 3.9+
- Google ADK installed
- Required dependencies

### **Installation**

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment:**
   ```bash
   # Add any required API keys to .env file
   # The project includes mock implementations for demonstration
   ```

### **Running with ADK Web**

1. **Start ADK Web interface:**
   ```bash
   adk web
   ```

2. **Open browser** to `http://localhost:8000`

3. **Choose your architecture pattern:**

   **🔍 For Component Testing:**
   - Select `triage_agent`, `solution_agent`, or `action_agent`
   - Test individual components manually
   - Use for development and debugging

   **🎯 For Complete Automation:**
   - Select `customer_experience_rescue_swarm`
   - Get end-to-end resolution in single request
   - Use for demos and simple deployments

   **🚀 For Enterprise Workflows:**
   - Select `customer_rescue_orchestrator`
   - Get coordinated multi-agent resolution with full audit trail
   - Use for production deployments

## 💡 Architecture Patterns & When to Use Them

### **🎯 Architecture Decision Matrix**

| Requirement | Individual Agents | Consolidated Agent | Orchestrator |
|-------------|------------------|-------------------|--------------|
| **Simple Testing** | ✅ Perfect | ⚠️ All-or-nothing | ❌ Complex |
| **Production Deployment** | ❌ Complex coordination | ✅ Single deployment | ✅ Enterprise ready |
| **Debugging** | ✅ Isolated testing | ⚠️ Harder to isolate | ✅ Detailed logging |
| **Scalability** | ✅ Independent scaling | ⚠️ Monolithic | ✅ Distributed |
| **Maintenance** | ⚠️ Multiple deployments | ✅ Single codebase | ⚠️ Complex orchestration |
| **Audit Trail** | ❌ Manual tracking | ⚠️ Limited visibility | ✅ Complete workflow logs |
| **Error Recovery** | ⚠️ Manual intervention | ⚠️ All-or-nothing | ✅ Step-by-step recovery |

### **💡 When to Use Each Pattern**

#### **🔍 Use Individual Agents When:**
- Building and testing components in isolation
- Need fine-grained control over each step
- Debugging specific functionality
- Learning ADK agent patterns
- **Example**: "I want to test just the triage logic"

#### **🎯 Use Consolidated Agent When:**
- Simple deployment requirements
- End-to-end automation needed
- Limited infrastructure complexity
- Proof of concept or demos
- **Example**: "I want one agent that handles everything"

#### **🚀 Use Orchestrator When:**
- Enterprise production deployment
- Complex workflow requirements
- Detailed audit trails needed
- Error recovery and monitoring
- Multi-team development
- **Example**: "I need enterprise-grade customer service automation"

### **📈 Event Flow Comparison**

#### **Speed to Resolution:**
- **Individual Agents**: Slowest (manual coordination)
- **Consolidated Agent**: Fastest (automated workflow)
- **Orchestrator**: Medium (coordinated but comprehensive)

#### **Observability:**
- **Individual Agents**: Limited (per-agent only)
- **Consolidated Agent**: Medium (single agent view)
- **Orchestrator**: Highest (complete workflow visibility)

#### **Flexibility:**
- **Individual Agents**: Highest (complete control)
- **Consolidated Agent**: Lowest (fixed workflow)
- **Orchestrator**: High (configurable coordination)

## 🧪 Testing Examples by Pattern

### **Individual Agent Testing (Manual Workflow):**
```bash
# Step 1: Test Triage
Select: triage_agent
Input: "Analyze customer C67890 with transcript T12345 - extremely upset about damaged product"
Expected: Escalation decision with priority and recommended actions

# Step 2: Test Solution (using triage results)
Select: solution_agent  
Input: "Find solution for Gold Tier customer with damaged expensive item"
Expected: Ranked solution options with full refund recommendation

# Step 3: Test Action (using solution results)
Select: action_agent
Input: "Execute full refund for order O-9987 and send apology communication"
Expected: Refund confirmation and communication sent
```

### **Consolidated Agent Testing (Automated Workflow):**
```bash
# Single Request - Complete Resolution
Select: customer_experience_rescue_swarm
Input: "Customer C67890 with transcript T12345 is complaining about a damaged item they received. They said 'I will never buy from you again, this is the worst experience ever.'"

Expected Flow:
├── 🔍 Calls CRM_LOOKUP_TOOL → Gets Gold Tier, LTV $1500
├── 🔍 Calls TRANSCRIPT_RETRIEVAL_TOOL → Confirms severe dissatisfaction  
├── 💡 Calls POLICY_LOOKUP_TOOL → Gets Gold Tier damage policy
├── ⚡ Calls REFUND_TOOL → Processes $75.50 refund
├── ⚡ Calls SEND_COMMUNICATION_TOOL → Sends personalized apology
└── ✅ Returns: "Issue escalated and resolved: full refund processed. Customer notified via email."
```

### **Multi-Agent Orchestrator Testing (Coordinated Workflow):**
```bash
# Orchestrated Multi-Step Resolution
Select: customer_rescue_orchestrator
Input: "Orchestrate complete resolution for customer C67890 with transcript T12345. Customer is extremely angry about receiving a damaged expensive item and threatening to leave."

Expected Flow:
├── 🚀 STEP 1: TRIAGE COORDINATION
│   ├── Calls CRM + Transcript tools
│   └── Logs: "✅ TRIAGE DECISION: ESCALATE (Gold Tier + Severe Dissatisfaction)"
├── 🚀 STEP 2: SOLUTION COORDINATION  
│   ├── Calls Policy tools
│   └── Logs: "💡 SOLUTION PHASE: Recommending full refund with premium handling"
├── 🚀 STEP 3: ACTION COORDINATION
│   ├── Calls Refund + Communication tools
│   └── Logs: "⚡ ACTION PHASE: Refund processed, personalized communication sent"
└── ✅ Returns: Detailed workflow execution log with all coordination steps
```

## 📁 Project Structure

```
project/
├── shared_tools/                 # 🔧 Centralized tools library
│   ├── crm_tools.py             # Customer & transcript lookup tools
│   ├── action_tools.py          # Refund & communication tools  
│   ├── policy_tools.py          # Policy & order status tools
│   └── __init__.py              # Tool exports for easy importing
├── triage_agent/                # 🔍 Individual triage specialist
│   ├── agent.py                 # Triage logic + shared tools
│   └── __init__.py
├── solution_agent/              # 💡 Individual solution finder
│   ├── agent.py                 # Solution logic + shared tools
│   └── __init__.py
├── action_agent/                # ⚡ Individual action executor
│   ├── agent.py                 # Action logic + shared tools
│   └── __init__.py
├── customer_experience_rescue_swarm/ # 🎯 Consolidated agent
│   ├── agent.py                 # Complete workflow + shared tools
│   └── __init__.py
└── customer_rescue_orchestrator/ # 🚀 Multi-agent orchestrator
    ├── agent.py                 # Coordinates all agents
    └── __init__.py
```

## 🔧 Development

### **Adding New Tools**
1. Add tool function to appropriate file in `shared_tools/`
2. Wrap with `FunctionTool()` and export in `__init__.py`
3. Import and use in any agent

### **Adding New Agents**
1. Create new directory with `agent.py` and `__init__.py`
2. Import shared tools from `shared_tools`
3. Add agent-specific logic as needed
4. Agent will be automatically discoverable in ADK Web

### **Architecture Evolution**
- Start with individual agents for clear separation
- Use consolidated agent for simpler deployment
- Add orchestrator for complex multi-agent workflows
- Leverage shared tools for consistency

## 💡 Best Practices Demonstrated

1. **Tool Organization** - Shared tools vs agent-specific logic
2. **Code Reuse** - Eliminate duplication through centralized tools
3. **ADK Patterns** - Proper FunctionTool usage and agent structure
4. **Architecture Flexibility** - Multiple patterns for different use cases
5. **Maintainability** - Single source of truth for tool implementations

## 📝 Notes

- **Mock Data**: Project includes mock implementations for CRM, policies, etc.
- **ADK Version**: Built for Google ADK latest version
- **Production Deployment**: Ready for Google Cloud Agent Engine deployment
- **Extensibility**: Architecture supports easy addition of new agents and tools

---

## 📚 Detailed Implementation Guide

*For detailed event flows, architecture diagrams, and step-by-step implementation examples, see the sections below.*

<details>
<summary><strong>🔄 Detailed Event Flow & Architecture Patterns</strong></summary>

### **Request Entry Points**

The system supports **multiple entry points** depending on your architectural choice:

1. **Direct Agent Access** - User selects specific agent in ADK Web
2. **Consolidated Workflow** - Single agent handles complete process
3. **Orchestrated Multi-Agent** - Orchestrator coordinates multiple agents

### **🏗️ Architecture Diagrams**

#### **Pattern 1: Individual Specialized Agents**
```
👤 User Request
    ↓
🔍 triage_agent
    ↓ (manual handoff)
💡 solution_agent  
    ↓ (manual handoff)
⚡ action_agent
    ↓
✅ Resolution
```

#### **Pattern 2: Consolidated Agent Workflow**
```
👤 User Request
    ↓
🎯 customer_experience_rescue_swarm
    ├── calls CRM_LOOKUP_TOOL
    ├── calls TRANSCRIPT_RETRIEVAL_TOOL
    ├── calls POLICY_LOOKUP_TOOL
    ├── calls REFUND_TOOL
    ├── calls SEND_COMMUNICATION_TOOL
    └── uses process_customer_issue()
    ↓
✅ Complete Resolution
```

#### **Pattern 3: Multi-Agent Orchestration**
```
👤 User Request
    ↓
🚀 customer_rescue_orchestrator
    ├── Step 1: Calls CRM + Transcript tools
    ├── Step 2: Calls Policy tools for solution
    ├── Step 3: Calls Action tools for execution
    ├── Step 4: Calls Communication tools
    └── uses orchestrate_customer_issue()
    ↓
✅ Coordinated Multi-Step Resolution
```

### **📊 Detailed Event Flow Examples**

#### **🔍 Individual Agent Flow (Manual Coordination)**

**When User Selects `triage_agent`:**
```
1. 👤 User: "Analyze customer C67890 with transcript T12345"
2. 🔍 triage_agent:
   ├── calls CRM_LOOKUP_TOOL(customer_id="C67890")
   ├── calls TRANSCRIPT_RETRIEVAL_TOOL(transcript_id="T12345")
   └── calls make_triage_decision(ltv, status, sentiment)
3. 📋 Returns: Escalation decision with priority and actions
4. 👤 User manually proceeds to solution_agent with results
```

#### **🎯 Consolidated Agent Flow (Single Entry Point)**

**When User Selects `customer_experience_rescue_swarm`:**
```
1. 👤 User: "Customer C67890 with transcript T12345 is complaining about damaged item"

2. 🎯 customer_experience_rescue_swarm automatically:
   
   📍 TRIAGE PHASE:
   ├── calls CRM_LOOKUP_TOOL(customer_id="C67890")
   │   └── Returns: {"ltv": 1500, "status": "Gold Tier", "orders": 12}
   ├── calls TRANSCRIPT_RETRIEVAL_TOOL(transcript_id="T12345") 
   │   └── Returns: "very unhappy... damaged... never again..."
   └── Internal logic: Severe dissatisfaction + High value = ESCALATE
   
   📍 SOLUTION PHASE:
   ├── calls POLICY_LOOKUP_TOOL(query="damaged item Gold Tier customer")
   │   └── Returns: "Full refund or express replacement for Gold customers"
   └── Internal logic: Select full refund based on policy
   
   📍 ACTION PHASE:
   ├── calls REFUND_TOOL(order_id="O-9987", amount=75.50)
   ├── calls SEND_COMMUNICATION_TOOL(customer, "email", apology_message)
   └── calls process_customer_issue() for workflow coordination

3. ✅ Returns: "Issue escalated and resolved: full refund processed. Customer notified via email."
```

#### **🚀 Multi-Agent Orchestration Flow (Coordinated Entry Point)**

**When User Selects `customer_rescue_orchestrator`:**
```
1. 👤 User: "Orchestrate complete resolution for customer C67890 with damaged item"

2. 🚀 customer_rescue_orchestrator coordinates:

   📍 STEP 1: TRIAGE COORDINATION
   ├── calls CRM_LOOKUP_TOOL(customer_id="C67890")
   ├── calls TRANSCRIPT_RETRIEVAL_TOOL(transcript_id="T12345")
   ├── Logs: "🔍 TRIAGE PHASE: Customer Gold Tier (LTV: $1500)"
   └── Decision: "✅ TRIAGE DECISION: ESCALATE"
   
   📍 STEP 2: SOLUTION COORDINATION  
   ├── calls POLICY_LOOKUP_TOOL(query="damaged item Gold Tier customer")
   ├── Logs: "💡 SOLUTION PHASE: Policy retrieved for high-value customer"
   └── Decision: "Best solution: full_refund with premium handling"
   
   📍 STEP 3: ACTION COORDINATION
   ├── calls REFUND_TOOL(order_id="O-9987", amount=75.50)
   ├── calls SEND_COMMUNICATION_TOOL(customer, "email", personalized_message)
   ├── Logs: "⚡ ACTION PHASE: Refund processed, communication sent"
   └── calls orchestrate_customer_issue() for detailed workflow logging

3. ✅ Returns: Detailed multi-step workflow log with all coordination steps
```

</details>

---

This implementation demonstrates **enterprise-grade agent architecture** with proper separation of concerns, zero code duplication, and multiple architectural patterns for different use cases.
