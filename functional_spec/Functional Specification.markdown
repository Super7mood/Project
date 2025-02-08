> **Table of Contents**
>
> **1. Introduction**\
> 1.1 Overview\
> 1.2 Purpose\
> 1.3 Document Conventions\
> 1.4 Scope\
> 1.5 Document Outline\
> 1.6 Glossary\
> **2. General Description**\
> 2.1 Product/System Functions\
> 2.2 User Characteristics and Objectives\
> 2.3 Operational Scenarios\
> 2.4 Constraints\
> **3. Functional Requirements**\
> 3.1 Output Type Selection\
> 3.2 Question Categorization\
> 3.3 Prompt Handling\
> 3.4 Prompt Optimization\
> 3.6 LLM Response Collection\
> 3.7 Similarity Comparison\
> 3.8 Historical Accuracy Benchmarking\
> 3.9 Composite Scoring System\
> 3.10 Ranking Responses\
> 3.11 Autonomous Evaluation\
> 3.12 Error Management\
> **4. System Architecture**\
> 4.1 System Architecture Diagram (Fig 1.1)\
> 4.2 Architectural Components\
> **5. High-Level Design**\
> 5.1 High-Level Design Diagram (Fig 1.2)\
> 5.2 High-Level Design Description\
> **6. Preliminary Schedule**\
> 6.1 Overview of Preliminary Schedule\
> 6.2 PERT and GANTT Charts (Fig 1.3, Fig 1.4)\
> **7. Appendices**\
> 7.1 LLM Websites
>
> 1\. **[Introduction]**
>
> **1.1 Overview**
>
> The proposed system, AICheckerPro , is designed to use multiple Large
> Language models (LLMs) such as chatgpt-4o, Gemini 1.5 flash, claude
> 3.5 Sonnet, mistral large, to improve reliability and accuracy of
> responses to user queries. The Primary goal of is to address a common
> issue with LLMs and their tendency to generate incorrect or misleading
> answers.
>
> To minimise this issue we have developed a system that utilises an
> easy to use interface where users can submit questions. These
> questions are then sent to multiple LLMs, each running its own
> response. The system then collects the responses from all LLMs and
> evaluates them using a range of metrics, including response
> similarity, the historical accuracy of each model and statistical
> analysis to identify the most reliable answer, which will then be
> presented to the user.
>
> To achieve this, the system will start a manual evaluation process,
> where predefined questions or queries will be tested across multiple
> LLMs, each response will be manually scored on accuracy, relevance and
> completeness. This initial phase will guide the development of an
> automated algorithm for scoring and combining responses from multiple
> LLMs.
>
> In conclusion, AICheckerPro aims to provide users with accurate
> information by carefully combining multiple AI perspectives. This
> system will be presented on a user-friendly Web-based interface where
> users can interact with the system in an easy and straightforward
> manner.
>
> **1.2 Purpose**
>
> This document is intended to achieve the functional, technical, and
> design part of AICheckerPro system specifications. It makes use of
> multiple Large Language Models (LLMs) to provide accurate and
> dependable answers to the queries posed by users. This system attempts
> to overcome imperfections and hallucinations of these individual LLMs
> by creating a framework for evaluating, ranking, and presenting
> answers.
>
> **In particular, the document will:**\
> ➢​ Define the goals & objectives of AICheckerPro.
>
> ➢​ Give very specific technical details for how the system could be
> built and tested.
>
> ➢​ Provide a guide for developers in the course of the entire project
> phase.
>
> **The intended audience includes:**
>
> ➢​ Project Supervisors: To evaluate project feasibility and
> performance.
>
> ➢​ Developers: To use as standard to develop and test the system.➢​ End
> Users: How the system will improve reliability and usability of
> AI-generated responses
>
> **1.3 Document Conventions**
>
> This document adhere to the following conventions for the sake of
> clarity and consistency :
>
> **Formatting:**\
> ➢​ Strong Text: Identifies section titles, or significant words.
>
> ➢​ Placeholder or Example: Italics\
> ➢​ Monospaced Text : For block of code, API or system command.
>
> **Terminology:**\
> ➢​ LLM "Large Language Models", like GPT-4, Claude, Gemini 1.5 and
> FlashClaude 3.5\
> ➢​ API Gateway: It acts as a gateway between the User Interface and
> backend services.
>
> ➢​ Firebase Database: It will store logs for historical-data and user
> interaction logs.
>
> **Figures and Tables:**\
> ➢​ Figures are sequentially numbered (i.e., Figure 1, Figure 2). 1.1).
>
> ➢​ All tables have titles and are cited in the text.
>
> ➢​ All definitions and technical terms are included in Section 1.6:
> Glossary for quick reference.
>
> **1.4 Scope**
>
> The project AICheckerPro seeks to implement an online Web- based
> platform capable of:\
> ➢​ Combining multiple LLM APIs to provide accuracy and reliability of
> answers. ➢​ Takes the intended responses and standardizes and evaluates
> responses using predefined metrics such as accuracy, relevance, and
> completeness. ➢​ Ranks and displays responses in an interactive way.
>
> ➢​ Facilitates iteration and improvement with historical data analysis
> and integration.
>
> **Key Features:**
>
> ➢​ **Multi-model integration**: allow for queries to be spread against
> numerous LLMs at once\
> ➢​ **Response processing:** Converts outputs in order to make them
> easily comparable.
>
> ➢​ **Scoring and Ranking**: It uses algorithms to score responses and
> then rank them based on certain (defined) metrics.
>
> ➢​ **User interface:** The API has a smooth feel to it, making it
> easier for the user to post queries and visualize results.
>
> **Out of Scope:**
>
> ➢​ Advanced machine learning models\
> ➢​ Allows on-premises LLMs (with a focus only on API-based access).
>
> ➢​ Too many LLMs as we would not have enough time to integrate a large
> amount of LLMs\
> ➢​ This will help to ensure the project is manageable in the given
> timeframe and budget, with a functional prototype as an output.
>
> **1.5 Document Outline**
>
> **Introduction:** Provides an overview, purpose, scope, and
> conventions used in this document.
>
> **General Description:** Outlines system functions, user
> characteristics, and operational scenarios.
>
> **Functional Requirements**: Details the key features and technical
> requirements of the system.
>
> **System Architecture:** Describes the overall architecture, including
> diagrams and component details.
>
> **High-Level Design:** Provides a detailed description of the system's
> design and data flow.
>
> **Preliminary Schedule:** Outlines the project timeline, including
> development phases and milestones.
>
> **Appendices:** Contains supporting materials, references, and
> additional documentation.
>
> **1.6 Glossary**
>
> **LLM** (Large Language Model): These are foundation models trained on
> immense amounts of data making them capable of understanding and
> generating natural language and other types of content to perform a
> wide range of tasks.
>
> **Chatgpt-4o:** A version of the OpenAI language model used as one of
> the multiple LLMs. This model generates natural language responses
> based on the user\'s input.
>
> **Gemini 1.5 flash:** Another LLM developed by a separate provider
> used to enhance the diversity of responses.
>
> **Claude 3.5 Sonnet:** Another LLM integrated into AICheckerPro
> contributing to the multi-model approach for providing accurate
> answers.
>
> **Mistral large:** One of the LLM used in AICheckerPro to broaden the
> perspectives considered when generating a response or answer.
>
> **API** (Application Programming Interface): A set of protocols that
> allows one software application to interact with another.
>
> **Hallucinations**: These are instances where an LLm generates an
> inaccurate response
>
> **Python:** A high- level programming language used for back-end
> development particularly for making API calls to LLMs and handling
> data processing.
>
> **Javascript:** A programming language used for creating interactive
> elements within the user interface.
>
> **HTML (HyperText Markup Language):** The standard language used for
> creating the structure of web pages.
>
> **CSS (Cascading Style Sheet):** language used to control the
> presentation of the web pages.
>
> **Node.js:** A back-end javascript runtime environment used to handle
> server-side operations.
>
> **React.js:** A JavaScript library used for building the user
> interface.
>
> **JSON (JavaScript Object Notation) :** A lightweight data format used
> to structure the responses from LLMs.
>
> **FireBase:** A platform developed by Google that is used to manage
> our user data and potentially storing messages and interaction logs.
>
> 2\. **[General Description]**
>
> **2.1 Product/System Functions**
>
> The following functions will be implemented in the AI Checker Pro
> system to ensure efficient and accurate delivery of optimal answers to
> user's queries:
>
> ●​ User Input Handling:\
> ○​ This function shall allow the user to input a question or prompt
> into the system. The input is processed and prepared for evaluation.
>
> ●​ Selection of Answer Type:\
> ○​ Provides users with options like number, word, two words, phrase,
> paragraph, etc., to define the expected format of the answer for
> accurate answer matching.
>
> ●​ Prompt Type:\
> ○​ Allows users to select the question category, like math, fact-based,
> or descriptive, to be more accurate in the performance and outcomes of
> AI.
>
> ●​ Ai API Call:\
> ○​ Handles communication with several AI models, sending the user\'s
> prompt to all integrated AIs with clear instructions on the structure
> of the answer and retrieving their responses efficiently.
>
> ●​ Answer Accuracy Evaluation:\
> ○​ Utilizes pre-stored accuracy scores for each AI model, based on a
> history of manual evaluations, to weigh the reliability of their
> responses.
>
> ●​ Answer Similarity Analysis:\
> ○​ Compares the answers returned by different AIs using a similarity
> algorithm to assess the closeness of responses to the user\'s query.
>
> ●​ Answer Ranking:\
> ○​ Combines accuracy scores and similarity analysis results to rank the
> answers in order of relevance and reliability.
>
> ●​ Optimal Answer Selection:\
> ○​ Identifies the best answer by applying a ranking mechanism that
> considers both accuracy scores and contextual relevance.
>
> ●​ Answer Presentation:\
> ○​ Delivers the chosen optimal answer to the user in their preferred
> format with a ranking of other potential answers for comparison.
>
> ●​ Data Management:\
> ○​ Stores and retrieves scores related to accuracy, and also system
> data, on a secure Firebase database with a scalable and reliable
> model.
>
> **2.2 User Characteristics and Objectives**
>
> AI Checker Pro is meant for anyone wanting to get accurate answers to
> their queries. It would include students from around the world,
> professionals, and\
> researchers and some casual users having limited tech-savvy abilities.
> It seeks to be more accessible by requiring the least amount of
> technical savvy since all that the user would have to do is input his
> or her question and select the more preferred format of the answer
> like number, word, phrase, or paragraph, and there it serves the
> answer to the user. Users would look forward to efficiency,
> reliability, and simplicity in a system, which means that the expected
> answer will be factually correct and contextually relevant without any
> unnecessary complication. Although users need not know either of the
> methods, they do want at least some transparency into ranking or
> selection to instil confidence in the system outputs.
>
> **2.3 Operational Scenarios**
>
> The following scenarios describe how users interact with the AI
> Checker Pro system under various conditions. These scenarios
> illustrate end-to-end transactions from the user\'s perspective,
> detailing how the system responds to their inputs and delivers
> outputs.
>
> **Scenario 1: General User Queries a Fact-Based Question**
>
> ●​ Description: One of the users is trying to know the capital of
> France, enters a factual question (e.g., \"What is the capital of
> France?\") into the system. They choose the answer type \"Word\" and
> category \"Fact\" through the provided drop-down menus.
>
> ●​ Steps:\
> 1.​ The user initiates the system and types their query.
>
> 2.​ The user chooses \"Word\" and \"Fact\" respectively for the answer
> type and category.
>
> 3.​ The system sends the query to AI models through API\
> 4.​ Data is retrieved and is analyzed according to accuracy scores and
> similarities.
>
> 5.​ The preferred answer, which is \"Paris,\" is shown to the user
> along with the ranking list of alternative answers.
>
> **Scenario 2: User Seeks a Numerical Answer**
>
> ●​ Description: A user issues the question \"What is 12 multiplied by
> 15? and then selects \"Number\" and \"Math\" as the expected answer
> and category,\
> respectively.
>
> ●​ Steps:\
> 1.​ The user types the question followed by choosing \"Number\" and
> \"Math\" in the system.
>
> 2.​ The system processes the question and then sends it to the AI
> models.
>
> 3.​ The system determines the scores obtained by the models and the
> similarity to the user\'s question.
>
> 4.​ The optimal answer, \"180,\" is visible to the user together with
> the confidence scores.
>
> **Scenario 3: User Requires a Detailed Explanation**
>
> ●​ **Description**: A user asks an open-ended question (e.g., \"Explain
> how\
> photosynthesis works.\") and selects \"Paragraph\" as the expected
> answer type and \"Fact\" as the prompt category.
>
> ●​ **Steps**:\
> 1.​ The user inputs the question and specifies \"Paragraph\" and
> \"Fact.\"
>
> 2.​ The system sends the question to the AI models and
> retrieves multiple detailed responses.
>
> 3.​ Answers are analyzed for similarity, accuracy, and coherence.
>
> 4.​ The best response is displayed to the user, formatted as a
> paragraph with an option to view alternative responses.
>
> **Scenario 4: System Handles Ambiguous Input**
>
> ●​ **Description**: A user enters a vague question (e.g., \"How tall is
> the Eiffel Tower?\") without specifying the answer type or category.
>
> ●​ **Steps**:\
> 1.​ The user inputs the question but skips specifying the answer type
> or category.
>
> 2.​ The system identifies potential answer types based on context
> (e.g., \"Number\").
>
> 3.​ The prompt is sent to AI models, and responses are retrieved and
> analyzed.
>
> 4.​ The system determines the optimal answer (\"324 meters\") and
> presents it to the user with additional context about the selection.
>
> **Scenario 5: User Interacts with Updated Accuracy Scores**
>
> ●​ **Description**: After accuracy scores for one or more AI models are
> updated in the database, a user queries a question (e.g., \"What is
> the boiling point of water?\").
>
> ●​ **Steps**:\
> 1.​ The system uses the updated accuracy scores from the Firebase
> database when evaluating responses.
>
> 2.​ The user\'s question is sent to the AI models, and responses are
> retrieved.
>
> 3.​ The system combines updated accuracy data with similarity analysis
> to rank the answers.
>
> 4.​ The optimal answer (\"100°C\") is displayed, reflecting the
> improved system accuracy.
>
> **2.4 Constraints**
>
> Below is a list of possible constraints placed upon the design team
> under which this project will be developed.
>
> **_Time constraints_**
>
> The project has a completion due date for DCU and this is due 5pm
> Friday 21st Feb 2025.
>
> **_Data Management Constraints_**
>
> All accuracy scores and related data must be securely stored and
> retrieved from Firebase. Data security and integrity are critical, and
> the database must handle scalability as the number of queries and
> users grows.
>
> **_Financial Constraints_**
>
> The project must work within a minimum budget. As APIs require credit
> to be able to be called, This may require prioritizing the use of
> open-source tools and cost-efficient cloud services such as Firebase
> for database management and finding alternative cost effective methods
> to call the APIs.
>
> **_Compliance Constraints_**
>
> The system must comply with all relevant industry standards, including
> API usage policies and data privacy regulations. Ensuring compliance
> will avoid legal and operational issues during deployment.
>
> **_Prompt Type Constraints_**
>
> The system must handle and provide a few types and format of prompts
> because there are indefinite structures and types of prompts which
> will not be feasible to score the accuracy of each AI chatbot to all
> structures and types of prompts which help in getting the optimal
> response.
>
> .3. **[Functional Requirements]**
>
> **3.1 Output Type Selection**\
> **●​ Description:**\
> There will be a dropdown menu selection of the structure of the
> response the user will expect to get whether it's one word, a number,
> phrase, paragraph or a default answer. For instance, if the user asked
> "Who is the president of Ireland", instead of getting "As of 2024, the
> president of Ireland is...", they will just get the necessary
> information "Michael D. Higgins" if they selected a phrase.
>
> **●​ Criticality:**\
> It is important to reduce unnecessary information from LLMs response
> in order to analyse responses better, this requirement will help make
> answer comparison more efficient. Instead of comparing long responses
> from LLMs, comparing a word or a phrase or a paragraph will allow us
> to find similarities quicker and determine the most similar answer.
>
> **●​ Technical Issues:**\
> The dropdown menu will be designed in the front end in javascript. An
> issue could occur If the user picked the input as a number and asked a
>
> question requiring a word, it will cause unexpected behaviour from
> LLMs, which will require us to code algorithms to detect mismatch
> between prompt output type and prompt asked. Furthermore, it will
> require adding correct prompt engineering in python to ensure that the
> LLM response with the desired output format.
>
> **●​ Dependencies:**\
> none
>
> **3.2 Question Categorization**\
> **• Description:**\
> Similar to the previous requirement, the system will allow users to be
> able to pick the type of prompt they will be asking where they can
> identify a type of question as a math question or fact question or
> geography question.
>
> **• Criticality:**\
> The system has accuracy data on LLMs responses to various fields in
> question. By letting the user identify the field of the question, it
> will help the system identify the accuracy of LLMs on a specific field
> of prompts which will help on getting the optimal answer.
>
> **• Technical Issues:**\
> The Question categorization will be developed in javascript.
>
> **• Dependencies:**\
> none
>
> **3.3 Prompt Handling**\
> **• Description:**\
> After the user enters a prompt. The system will process and send the
> prompt to the backend alongside its selected output format and
> question types where it will be sent to LLMs.
>
> **• Criticality:**\
> This requirement is essential to ensure the accuracy and reliability
> of responses. Without proper validation, malformed prompts might
> result in irrelevant or incorrect answers.
>
> **• Technical Issues:**
>
> There has to be validations for the prompt in javascript where we will
> need to validate whether the prompt is empty or weather the prompt has
> enough long enough to be a valid query to LLMs\
> **• Dependencies:**\
> Output Type Selection, Question Categorization
>
> **3.4 Prompt Optimization**\
> **• Description:**\
> The system optimises the user's prompts in order to get the result in
> the desired structure as for the output type selected. This involves
> writing a set of instructions in the prompt to direct the api on the
> structure of the response
>
> **• Criticality:**\
> This function is important as it ensures that the output is in the
> right format and LLMs do not provide more information than necessary.
>
> **• Technical Issues:**\
> In Python, string manipulation needed to structure the prompt.
>
> **• Dependencies:**\
> Output Type Selection, Prompt Handling.
>
> **3.5 Multi-LLM Query Dispatch**\
> **• Description:**\
> The system sends user queries to multiple LLM APIs simultaneously to
> gather diverse responses for evaluation and comparison.
>
> **• Criticality:**\
> This requirement is essential as without it, the system loses its
> ability to assess answer quality across models.
>
> **• Technical Issues:**\
> In Python, asynchronous calls to APIs must be implemented for
> efficiency. In JavaScript, a loading indicator is needed to improve
> user experience while responses are fetched.
>
> **• Dependencies:**
>
> .Prompt Optimization.
>
> **3.6 LLM Response Collection**\
> **• Description:**\
> This system must collect and standardise responses from multiple LLMs.
> It ensures consistency in formatting for effective comparison.
>
> **• Criticality:**\
> This is highly critical to ensure that all responses can be processed
> uniformly. Without standardization, comparisons could fail due to
> inconsistencies.
>
> **• Technical Issues:**\
> In Python, accepting JSON formatting and validation of API responses
> are required.
>
> **• Dependencies:**\
> .Multi-LLM Query Dispatch
>
> **3.7 Similarity Comparison**\
> **• Description:**\
> The system calculates the semantic similarity between responses using
> techniques like cosine similarity. This helps identify overlapping or
> divergent answers.
>
> **• Criticality:**\
> This is critical for determining consensus among LLMs. Without it, the
> system cannot establish how closely answers align with each other.
>
> **• Technical Issues:**\
> Needs to identify and create suitable algorithms for comparison
>
> **• Dependencies:**\
> LLM Response Collection
>
> **3.8 Historical Accuracy Benchmarking**\
> **• Description:**
>
> The system evaluates responses based on the historical performance of
> each LLM on similar question types. Accuracy scores are stored and
> used in comparisons.
>
> **• Criticality:**\
> This requirement is critical as it adds a reliability factor to the
> scoring process. Without it, the system might overvalue responses from
> less consistent models.
>
> **• Technical Issues:**\
> Need to have the accuracy stored on firebase and called by python
> efficiently.
>
> **• Dependencies:**\
> LLM Response Collection,
>
> **3.9 Composite Scoring System**\
> **• Description:**\
> This system assigns a weighted score to each response by combining
> metrics like similarity, historical accuracy, and relevance. And it
> adds these weights in order to identify the best answer with the most
> weight.
>
> **• Criticality:**\
> This requirement is essential to rank responses effectively. Without
> it, the system cannot reliably identify the best answer between the
> LLM models.
>
> **• Technical Issues:**\
> We will design a suitable algorithm in python to calculate composite
> scores with adjustable weights.
>
> **• Dependencies:**\
> LLM Response Collection, Similarity Comparison, Historical Accuracy
> Benchmarking.
>
> **3.10 Ranking Responses**
>
> **• Description:**\
> Responses are ranked based on their composite scores, with the highest
> ranked answer considered as the optimal solution.
>
> **• Criticality:**\
> It isn't necessary to rank them when we can just get the one with the
> maximum weight, however, ranking helps in visualizing the LLMs that
> answered well and the LLMs that didn't
>
> **• Technical Issues:**\
> In Python, implementing an efficient sorting algorithm for ranked
> outputs is necessary. In JavaScript, dynamic tables or lists can be
> used to display ranked responses.
>
> **• Dependencies:**\
> LLM Response Collection, Composite Scoring System.
>
> **3.11 Autonomous Evaluation**\
> **• Description:**\
> The system must be able to accept files with question, output format,
> question and expected answers, and autonomously evaluate\
> responses.
>
> **• Criticality:**\
> It isn't mandatory to have this as we can manually check questions and
> answers with AI but it will speed the process up and allow us to\
> evaluate far more questions in a small window of time.
>
> **• Technical Issues:**\
> We will look at how to have the questions and answers in csv files and
> how to call it in python and how to automate the system to call it.
>
> **• Dependencies:**\
> Question Categorization, Prompt Handling, Prompt Optimization,
> Multi-LLM Query Dispatch, LLM Response Collection, Similarity
> Comparison, Historical Accuracy Benchmarking, Composite Scoring System
>
> **3.12 Error Management**
>
> **• Description:**\
> The system handles errors such as API timeouts or unresponsive LLMs
> gracefully, retrying failed calls and notifying users as needed.
>
> **• Criticality:**\
> This is critical for ensuring robustness and reliability. Without it,
> errors cause the system to malfunction.
>
> **• Technical Issues:**\
> In Python, retry mechanisms with exponential backoff need to be
> implemented. In JavaScript, real-time notifications for errors are
> essential.
>
> **• Dependencies:**\
> Multi-LLM Query Dispatch, LLM Response Collection
>
> 4\. **[System Architecture]**\
> **4.1 System Architecture Diagram (Fig 1.1)**
>
> ![](media/image1.png)
>
> In the above Fig (1.1)
>
> The System Architecture Diagram demonstrates the engineering of a
> proposed system. It emphasizes the movement of data and interaction
> throughout 8 different pieces. It has the User Interface (UI), that is
> the front-end of your system where users input queries and get ranked
> results. The other is API Gateway, which serves as a layer between the
> User Interface and backend; it redirects queries to LLM APIs. These
> are the API which manage the queries and take responses from you.
>
> These in-turn are processed by the Response Processor which
> preprocesses the data for evaluation. Evaluation Engine: It contains
> Scoring and Ranking Module to evaluate and rank the responses. It also
> includes a standard Firebase Database for saving the historical data
> and logs. The Output Formatter then formats the ranked responses and
> sends these to the user through the User Display.
>
> **4.2 Architectural Components**
>
> **User Interface**
>
> User Interface (UI): The part of the system that is readily available
> in a web browser. Users ask a question and receive ranked answers with
> an extremely user-friendly and responsive interface. It is built with
> HTML, CSS, and JavaScript frameworks (e.g., React), ensuring
> accessibility and usability.
>
> **API Gateway**
>
> The API Gateway box provides the interface between User Interface
> which calls API to communicate with backend services. Routes user
> queries to the appropriate Large Language Model (LLM) APIs, which are
> GPT-4, Claude, Gemini 1.5 and flash claude 3.5. These manages handling
> request authentication, rate limiting,and load\
> balancing etc
>
> **Large Language Model APIs**
>
> This component facilitates the integration of external AI models, such
> as GPT-4 and Claude, which are pivotal for generating responses to
> user queries. These APIs are accessed via secure endpoints. Each model
> processes queries independently, returning structured responses in
> formats such as JSON, ensuring compatibility with downstream
> components.
>
> **Response Processor**
>
> The Response Processor is a translation layer that sits between the
> LLM APIs and the scoring systems. It standardizes the outputs
> generated by the LLMs and fetches them (e.g., transforming responses
> into the same JSON structure).
>
> Accuray/efficiency of scoring requires the same scale across datasets,
> otherwise a
>
> process using this normalization would be necessary. To do that,
> custom scripts will get implemented that would enable the transfer of
> user data much more automated and simpler for rating exercises.
> Through Creating an Organized and Persistent Production Output. The
> Response Processor ensures seamless integration with the Scoring and
> Ranking modules.
>
> **Evaluation Engine**
>
> ➢​ **Scoring Module**: Sub-component that allows for the scoring of
> curated responses based on predefined metrics (e..g, accuracy,
> relevance,\
> completeness). Every response is analyzed with a custom algorithm,
> creating an objective and uniform scoring protocol that provides an
> even basis to compare answers.
>
> ➢​ **Ranking Module:** Takes the scores from the Scoring Module and
> ranks the responses in an ordered list. then this output is shown to
> the user. Ranked output is now clear and relevant, ready to be
> presented to the user.
>
> **Firebase Database**
>
> This database is used to store everything happening on the user side.
> it is a log file for all the user\'s actions and server outputs. It
> aids the Evaluation Engine in\
> accessing previously calculated accuracy scores and storing new
> results produced. The database is designed to allow for iterative
> improvements through storing data in a way that can be used again
> during future assessments.
>
> **Output Formatter**
>
> The Output Formatter, This component collates ranked responses
> generated by the Evaluation Engine and makes them ready for user
> friendly display. Provides a way to transition between processing in
> the backend with rendering in the front-end.
>
> Adhering to the User Interface design. Outputs are structured in JSON
> or HTML formats, balancing clarity with technical compatibility.
>
> **User Display**
>
> The User Display, which is the user-facing component that displays and
> ranks results to users. Optimized for visual clarity, it brings the
> best answer to the forefront and also allows some space to survey
> alternative answers by users. A neat and pretty interface that helps
> to perform usability techniques and normal statistical results very
> easily
>
> 5\. **[High-Level Design]**\
> **5.1 High-Level Design Diagram (Fig 1.2)**

![](media/image2.png)

> **5.1 High-Level Design Description**
>
> The system is designed to evaluate and rank responses from multiple
> Large Language Models (LLMs) through a seamless workflow. The
> following describes each component and its role in the system:
>
> **User Interface**\
> ➢​ The place where users can simply ask the questions.
>
> ➢​ Rank content with a sleek and responsive layout.
>
> ➢​ Focuses on Audience accessibility and Ease of use such as device
> used, format etc.
>
> **API Gateway**\
> ➢​ It is a bridge between User Interface and backend services.
>
> ➢​ It verifies the queries asked by users and redirects them to correct
> LLM APIs.
>
> ➢​ Secure and fast data download, also handles parallel API calls
>
> **Large Language Model APIs**\
> ➢​ Contains LLMs such as GPT-4, Claude, Gemini 1.5 and flash claude 3.5
> these can process each user query independently.
>
> ➢​ Creates secure, privacy-oriented responses to API calls.
>
> ➢​ Returns structured outputs (e.g., JSON format) for further
> processing.
>
> **Response Processor**\
> ➢​ Normalizing and standardising LLM API outputs.\
> ➢​ Is used to score and rank the responses.
>
> **Evaluation Engine**\
> ➢​ Scoring Module, scores the responses on metrics like how accurate,
> relevant and complete they are.
>
> ➢​ Ranking is the item that orders responses based on score, generating
> a ranked list of best answers.
>
> **Firebase Database**\
> ➢​ Stores all history scores, user interaction, and logs.
>
> ➢​ Feeds historical data to the Evaluation Engine for iteration
> improvements➢​ Supports reliable data retrieval and storage.
>
> **Output Formatter**\
> ➢​ Processes raw evaluation output into human-understandable format.➢​
> Conform to UI design principles.
>
> ➢​ Organizes responses for displaying in rank order.
>
> **User Display**
>
> ➢​ Ranked response provider to users.
>
> ➢​ How It Works: shows you the highest scored answers and lets you
> browse through the various response options.
>
> ➢​ Ensures clarity and usability in the presentation.
>
> 6\. **[Preliminary Schedule]**
>
> **6.1 Overview of Preliminary Schedule**
>
> The development schedule included below describes the major components
> of the project and gives a rough estimate of how long each will take
> to complete. This initial draft is tentative and may require revision
> as the project matures in order to address unforeseen obstacles or
> optimization-points.
>
> The final two weeks are at the end, which is to write up the final
> documentation and prep for their demonstration code. If any critical
> issues pop up during development, this time can be reassigned earlier
> to ensure they are addressed properly.
>
> **Code Review**
>
> ➢​ Study and optimize the original codebase to connect with LLM APIs
> and Firebase.
>
> ➢​ Comply with the design guidelines defined in the Functional
> Specification, and High-Level Design sections.
>
> ➢​ Fix any pre-existing issues in the implementation.
>
> **API Integration**
>
> ➢​ Build and rigorously test the API Gateway needed for enabling
> communication to chosen LLM APIs (eg. GPT-4, Claude)\
> ➢​ Have systems in places to ensure that data exchange is secure and
> good with external systems.
>
> ➢​ Make it scalable to handle parallel API requests.
>
> **Response Processor Implementation**
>
> ➢​ Implementing the Response Processor, standardizing and normalizing
> responses from LLM APIs.
>
> ➢​ Validate Processed Data Preparation Are Compatible with Scoring and
>
> **Scoring and Ranking Modules**
>
> ➢​ Check the functionality of high-response loads.
>
> ➢​ Scoring and Ranking Modules\
> ➢​ Run the Scoring Module on each response and score on a predefined
> range (e.g. 1--50) → (64-100). The Score should be relative to how
> accurate, relevant and complete the Response is.
>
> ➢​ Create the Ranking Module so it can order comments in order to
> create ranked outputs efficiently.
>
> ➢​ Iterations of tests will be conducted to fine tune testing
> algorithms.
>
> **Firebase Database Setup**
>
> ➢​ Configure the Firebase Database for storing historical scores, user
> interactions, and logs.
>
> ➢​ It should store data in a useful way so that it can be run against
> by the Evaluation Engine.
>
> ➢​ Load tests which validate the scalability and performance of the
> database.
>
> **Output Formatter Development**
>
> ➢​ Either way, the Output Formatter is responsible for converting the
> raw evaluation outputs into a user-friendly structure.
>
> ➢​ Ensure to line up the output form with UI/UX principles, in order
> for the user experience to remain consistent across your service.
>
> ➢​ Conduct edge cases for the formatter such as highly similar or
> conflicting scores.
>
> **Interface and Display**
>
> ➢​ Design and finalize the User Interface (UI) and Display component
> functions.➢​ Do usability testing to ensure the accessibility on
> different devices and screen sizes.
>
> ➢​ Iterate process as needed for clarity and to make sure users are
> happy with the product.
>
> **Documentation and Demonstration**
>
> ➢​ All technical writing including documentation of the feature.
>
> ➢​ User Manual: Guide for end users\
> ➢​ Specification: Description of what the software is supposed to do.
>
> ➢​ System Requirements : In-depth description of the system
> architecture and implementation.
>
> ➢​ Develop demonstration code to showcase the system\'s features and
> capabilities during evaluation.
>
> **6.2 PERT and GANTT Charts (Fig 1.3, Fig 1.4)**
>
> **GANTT Chart (Fig 1.3)**
>
> ![](media/image3.png)
>
> **PERT Chart (Fig 1.4)**
>
> ![](media/image4.png)
>
> 7\. **[Appendices]**
>
> 7.1 [LLM websites:]
>
> 1- https://openai.com/index/chatgpt/
>
> 2- https://claude.ai/new
>
> 3- https://gemini.google.com/app
