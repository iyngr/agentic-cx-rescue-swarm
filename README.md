# Agentic Customer Experience Rescue Swarm

A multi-agent system built with **Google Agent Development Kit (ADK)** that proactively handles customer issues based on sentiment analysis of call transcripts. Features **clean architecture** with **zero code duplication** and follows **ADK best practices**.

## 🏗️ Clean Architecture Overview

This project demonstrates **multiple agent patterns** you can use with ADK:

- **Individual Specialized Agents** - Triage, Solution, and Action agents that work independently
- **Consolidated Agent** - Single agent handling the complete workflow  
- **Multi-Agent Orchestrator** - Coordinates multiple agents working together
- **Shared Tools Library** - Centralized, reusable tools eliminating code duplication

All agents use **shared tools** from a centralized library, ensuring **zero code duplication** and **easy maintenance**.

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

3. **Select any agent** from the dropdown:
   - `triage_agent` - Test triage functionality
   - `solution_agent` - Test solution finding
   - `action_agent` - Test action execution
   - `customer_experience_rescue_swarm` - Test complete workflow
   - `customer_rescue_orchestrator` - Test multi-agent coordination

### **Testing Examples**

#### **Individual Agent Testing:**
```
Triage Agent: "Analyze customer C67890 with transcript T12345"
Solution Agent: "Find solution for Gold Tier customer with damaged item"  
Action Agent: "Execute full refund for order O-9987"
```

#### **Complete Workflow Testing:**
```
Consolidated Agent: "Customer C67890 with transcript T12345 is complaining about a damaged item"

Multi-Agent Orchestrator: "Orchestrate complete resolution for customer C67890 with damaged item complaint"
```

## 🎯 Architecture Patterns Demonstrated

### **1. Shared Tools Pattern**
- Centralized tool library
- FunctionTool wrapper usage
- Import and reuse across agents

### **2. Individual Agent Pattern**
- Specialized, single-responsibility agents
- Agent-specific business logic
- Tool composition for specific domains

### **3. Consolidated Agent Pattern**  
- Single agent handling complete workflow
- Internal workflow orchestration
- Simplified deployment and management

### **4. Multi-Agent Orchestration Pattern**
- Agent coordination and communication
- Workflow state management
- Inter-agent data passing

## 🔍 Key Features

- **🏗️ Clean Architecture** - Zero code duplication, proper separation of concerns
- **🔧 Shared Tools** - Centralized, reusable tool library
- **🎯 Multiple Patterns** - Individual, consolidated, and orchestrated agents
- **✅ ADK Compliance** - Proper FunctionTool patterns and agent discovery
- **🧪 Testable** - Individual tools and agents can be tested in isolation
- **📊 Observable** - Detailed logging and workflow tracking
- **🚀 Production Ready** - Follows best practices for maintainability

## 💡 Best Practices Demonstrated

1. **Tool Organization** - Shared tools vs agent-specific logic
2. **Code Reuse** - Eliminate duplication through centralized tools
3. **ADK Patterns** - Proper FunctionTool usage and agent structure
4. **Architecture Flexibility** - Multiple patterns for different use cases
5. **Maintainability** - Single source of truth for tool implementations

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

## 📝 Notes

- **Mock Data**: Project includes mock implementations for CRM, policies, etc.
- **ADK Version**: Built for Google ADK latest version
- **Production Deployment**: Ready for Google Cloud Agent Engine deployment
- **Extensibility**: Architecture supports easy addition of new agents and tools

This implementation demonstrates **enterprise-grade agent architecture** with proper separation of concerns, zero code duplication, and multiple architectural patterns for different use cases.
