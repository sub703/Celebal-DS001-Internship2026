# Single Agent Systems and Agent Pipelines Quiz

**1. Explain the concept of a stateful directed graph in agent pipelines. How does it differ from a simple linear pipeline?**

A stateful directed graph is a way of building a workflow where every step can remember and reuse information from the steps that came before it. The workflow is made of nodes, which are the tasks, and edges, which are the connections that decide where the data goes next. Because it holds on to state, it can branch into different paths, loop back when it needs to, and make decisions as it runs. A simple linear pipeline just runs one step after another in a fixed order and forgets what happened earlier, so it cannot change direction or react to what it found along the way. In short, the graph is flexible and aware of context, while the linear pipeline is rigid and stateless.

**2. Describe the role of nodes and edges in an agent workflow. Give an example of each.**

Nodes are the individual units of work in a workflow. Each node does one thing, like reading a query, calling a tool, or writing a response. Edges are the links between nodes that control how information moves from one step to the next. For example, a node could be the Calculator Tool that solves a math expression, and an edge could be the path that carries the query from the intent check into that calculator node. Put simply, the nodes do the work and the edges decide the order and the flow.

**3. What is conditional routing in an agent system? Design a simple rule based routing logic for three different query types.**

Conditional routing means sending each query to a different tool or action depending on what the user is actually asking for. It lets the agent pick the right handler instead of treating everything the same way. A simple rule based version for three query types could look like this: if the query contains the word "calculate", send it to the Calculator Tool; if it contains the word "keywords", send it to the Keyword Extraction Tool; and if it matches neither, pass it to a General Response handler that answers directly. The rules are checked in order, so the first one that matches decides the route.

**4. Why are cycles (loops) important in agent pipelines? Provide a use case where a retry loop is necessary.**

Cycles or loops let an agent repeat a step until it gets a result it is happy with, instead of giving up after a single try. They matter because real tasks fail sometimes, and one failure should not break the whole workflow. A common example is a retry loop around an API call. If the request fails because of a brief network glitch or a rate limit, the agent can wait a moment and try again a few times before it finally reports an error. That makes the system far more reliable than one which stops the instant something goes wrong.

**5. Explain how a single agent system can simulate multi agent behavior internally.**

A single agent can act like several agents by splitting its own work into separate roles and moving through them one at a time. It might first play the part of an analyst that reads and understands the query, then act as a router that decides which tool fits, and finally behave like a responder that produces the answer. Each of these roles feels like its own little agent, even though the same program runs all of them. This gives you the clarity of a multi agent design without the extra cost of actually running many agents at once.

**6. What are JSON schema tools? How do they help in structuring tool inputs and outputs?**

JSON schema tools describe the exact shape that data should take when it moves between the agent and its tools. A schema spells out which fields are required, what type each field should be, and how the output should be formatted. Before the agent runs a tool, it can check the input against the schema to make sure nothing important is missing or malformed. It also keeps the outputs consistent, so the rest of the system always knows what to expect. Overall this cuts down on errors and helps the different parts of the agent talk to each other cleanly.

**7. Compare sequential tool calls and parallel tool calls. When would you prefer one over the other?**

Sequential tool calls run one after the other, where each call waits for the previous one to finish because it needs that result to continue. Parallel tool calls run several independent tasks at the same time. You would prefer sequential calls when the steps depend on each other, for example when you have to fetch data first and only then process it. You would prefer parallel calls when the tasks have nothing to do with each other, since running them together can save a lot of time and make the agent feel much faster.

**8. How would you implement error handling in a tool using agent? Provide at least two strategies.**

Error handling keeps an agent working even when something breaks partway through. One simple strategy is to wrap risky operations in try and except blocks, so that an exception is caught and turned into a clear, friendly message instead of a crash. A second strategy is to add retry logic that automatically repeats an operation that failed for a temporary reason, which is handy for flaky network calls. It also helps to log every error as it happens, since good logs make debugging and monitoring much easier later on. Used together, these habits make the agent more stable and more pleasant to use.

**9. What is trajectory evaluation in agent systems? Why is it important beyond just checking final output?**

Trajectory evaluation looks at the whole path an agent took to reach an answer, not just the answer itself. It studies the decisions it made, the tools it called, and the intermediate steps it went through along the way. This matters because an agent can sometimes land on the right final output almost by luck while making poor choices in the middle, and a plain output check would never catch that. By inspecting the full trajectory, developers can see where the reasoning went wrong, fix inefficient routes, and steadily improve how the agent behaves.

**10. Define task completion rate and cost metrics. How would you measure and optimize them in a real world system?**

Task completion rate is the share of tasks that an agent finishes successfully out of everything it was asked to do. Cost metrics track the resources each task uses up, such as the number of API calls, the time taken, or the money spent. You can measure both by logging the outcome and the resource use of every task, and then looking at the totals over many runs. To improve them, you can sharpen the routing so queries reach the right tool the first time, cut out tool calls that are not needed, and pick faster methods where you can. The real goal is to keep the completion rate high while keeping the cost as low as you reasonably can.
