# Meadows Leverage Points Analyzer - Claude Skill (v2.0)

A Claude skill for analyzing systems and identifying intervention points using Donella Meadows' famous "12 Leverage Points" framework.

**Version 2.0** includes enhanced analysis framework, 7 example analyses, prioritization tools, and quick reference guide.

## What This Skill Does

This skill helps you:
- **Analyze any system** (business, social, technical, environmental)
- **Identify leverage points** where interventions can create change
- **Rank interventions** by effectiveness using Meadows' hierarchy
- **Get concrete recommendations** for system improvement

## Installation

This skill is already installed in your `.claude/skills/meadows-leverage-points/` directory.

## Usage

### Basic Usage

Simply describe a system you want to analyze:

```
Analyze this system: A software company where developers are always firefighting bugs
instead of building new features. Management keeps adding more developers but the
problem gets worse.
```

### Structured Input

For more detailed analysis, provide structured information:

```
Analyze this system:

**System**: Public transportation in City X
**Problem**: Low ridership despite investment
**Current state**:
- Buses run every 30 minutes
- No real-time arrival info
- Fares are high
- Routes don't connect well
- Cars are heavily subsidized (free parking, cheap gas)
```

### Specific Questions

Ask targeted questions:

```
What are the highest leverage points for improving employee retention in our company?
```

```
How can we intervene in this healthcare system to reduce costs?
```

## Example Analysis

### Input:
```
Analyze this system: An online learning platform where course completion rates are
only 5%. The company keeps adding more content and features, but completion rates
continue to decline.
```

### Output:
```
# System Analysis: Online Learning Platform

## System Overview
The platform exhibits a reinforcing feedback loop where low completion → more content
added to "fix" the problem → overwhelm increases → even lower completion. The system's
implicit goal appears to be "maximize content" rather than "maximize learning outcomes."

## Identified Leverage Points

### Goals (L3)
**Current State**: Implicit goal is content quantity; success measured by courses offered
**Intervention**: Redefine success as "completion rate" and "skills acquired"
**Expected Impact**: Fundamentally redirects all product decisions toward learner success
**Difficulty**: Medium - requires leadership buy-in but is achievable
**Risks**: May reduce revenue if business model depends on non-completing subscribers

### Information Flows (L6)
**Current State**: Learners lack feedback on progress; platform lacks data on why people drop off
**Intervention**: Add progress tracking, peer visibility, and drop-off analytics
**Expected Impact**: Learners get motivating feedback; company sees real problems
**Difficulty**: Low - mostly technical implementation
**Risks**: May reveal uncomfortable truths about content quality

### Positive Feedback Loop (L7)
**Current State**: More content → more overwhelm → less completion → "need more content"
**Intervention**: Break the loop by limiting content, focus on completion of existing courses
**Expected Impact**: Reduces overwhelm, improves completion, builds confidence
**Difficulty**: Medium - requires stopping current content production
**Risks**: Competitor might appear to have "more" offerings

[Additional leverage points...]

## Recommended Intervention Strategy

Start with **changing the goal** (L3) - shift metrics from content quantity to completion
and outcomes. This is high leverage and sets context for other changes. Immediately
follow with **information flow improvements** (L6) - make progress visible and collect
drop-off data. These two interventions will naturally reveal where to intervene next.

Avoid the temptation to just adjust parameters (e.g., changing the number of lessons,
adjusting video length) - these are low-leverage and don't address the fundamental
mismatch between the system's goal and user needs.
```

## Key Features

### Comprehensive Framework
- All 12 leverage points from Meadows' hierarchy
- Detailed descriptions and examples for each
- Clear ranking by effectiveness

### Concrete Recommendations
- Specific, actionable interventions
- Implementation difficulty assessment
- Risk and side-effect analysis

### Systems Thinking Approach
- Considers feedback loops and dynamics
- Identifies unintended consequences
- Focuses on structure over symptoms

## What's New in v2.0

**Enhanced Analysis Framework**:
- 4-phase structured process (Mapping → Identification → Prioritization → Design)
- System mapping templates for feedback loops, delays, and information gaps
- Prioritization matrix (Impact × Feasibility scoring)
- Anti-pattern recognition (8 common traps to avoid)
- Quick diagnostic checklist

**More Examples**:
- 7 detailed analyses (was 3): Traffic, Software Team Burnout, Social Media, Exercise Habits, ER Overcrowding, Marketplace Quality, Climate Change
- Covers personal, organizational, and societal systems
- Real-world patterns and lessons across domains

**Better Outputs**:
- Enhanced output format with system dynamics mapping
- Intervention roadmap (immediate/short-term/long-term)
- Alternative formats (Quick Scan, Workshop Guide)
- Priority scores and monitoring indicators

**Quick Reference Guide**:
- One-page cheat sheet (QUICK_REFERENCE.md)
- All 12 leverage points in table format
- Decision matrices and templates
- Common patterns by system type

## Files in This Skill

- **SKILL.md** - Main skill prompt with enhanced 4-phase framework
- **THEORY.md** - Detailed theory reference and background
- **EXAMPLES.md** - 7 detailed example analyses across domains
- **QUICK_REFERENCE.md** - One-page cheat sheet and templates
- **README.md** - This file (usage instructions)

## Tips for Best Results

1. **Describe the problem, not just the system**: What's not working? What behaviors do you see?

2. **Include dynamics**: How does the system behave over time? What patterns emerge?

3. **Mention attempted solutions**: What have you already tried? This helps identify low-leverage interventions to avoid.

4. **Provide context**: Who are the stakeholders? What are the constraints?

5. **Be specific**: Real details produce better analysis than generic descriptions.

## Understanding the Output

### Leverage Point Numbers (L1-L12)
- **L12-L9**: Physical and temporal (weak but easy)
- **L8-L6**: Feedback and information (moderate power)
- **L5-L3**: Structure and purpose (strong but harder)
- **L2-L1**: Paradigm and transcendence (strongest but hardest)

### Implementation Difficulty
- **Low**: Can be done quickly with existing resources
- **Medium**: Requires some organizational change or investment
- **High**: Requires significant change, leadership commitment, or cultural shift

## Common Use Cases

- **Business strategy**: Identifying where to focus improvement efforts
- **Product development**: Finding root causes of user problems
- **Organizational design**: Improving team dynamics and culture
- **Policy analysis**: Evaluating government or institutional interventions
- **Environmental systems**: Finding effective sustainability interventions
- **Social systems**: Understanding and improving community dynamics
- **Technical systems**: Debugging complex software or infrastructure issues

## Learning Resources

See `THEORY.md` for:
- Detailed explanation of each leverage point
- Common mistakes and how to avoid them
- Historical context and paradigm shift examples
- Further reading recommendations

## Limitations

- **Requires good system description**: Analysis quality depends on input detail
- **Not a substitute for domain expertise**: Combines systems thinking with your knowledge
- **Simplifies complex reality**: Models are useful but not complete
- **Context matters**: Same leverage point may work differently in different systems

## Version History

**v2.0** (Current):
- Enhanced 4-phase analysis framework
- 7 detailed examples across domains
- Prioritization matrix and scoring
- Anti-pattern recognition
- Quick reference guide
- System dynamics mapping
- Intervention roadmaps

**v1.0**:
- Basic leverage point identification
- 3 initial examples
- Simple output format

## Future Enhancements

Potential additions for v3.0:
- Interactive system mapping with visual diagrams
- Causal loop diagram generation
- Multi-system comparison and pattern matching
- Intervention sequencing and timing analysis
- Integration with stock-and-flow modeling
- Case study library with searchable patterns
- Leverage point decision trees

## Attribution

Based on the work of Donella Meadows (1941-2001), systems scientist and author of "Thinking in Systems" and the essay "Leverage Points: Places to Intervene in a System" (1999).

---

**Ready to analyze a system? Just describe it and let the skill guide you through the leverage points framework.**
