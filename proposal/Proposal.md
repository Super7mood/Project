**School of Computing**  
 **CSC1049 Year 3 Project Proposal Form**

**Project Title:** AICheckerPro

**Student 1 Name:**          Ayoub Al-Kendi                                	ID Number: 20106378                       **Student 2 Name:**          Connor Mcquillan                  	            ID Number: 20450192

**Staff Member Consulted:** Harshvardhan Pandit

***Description***

We propose to create a system called AICheckerPro, which will utilize multiple Large Language Models (LLMs) such as ChatGPT4, ChatGPT3, and Gemini to produce an optimal answer to a given question. The primary issue being addressed is that LLMs can sometimes provide incorrect or hallucinated answers, potentially leading users to misinformation. For example, if one were to ask ChatGPT4 how many "r's" are in the word "strawberry," it might incorrectly state there are two, which is inaccurate.

The system will feature an easy-to-use interface where users can submit questions. These questions will then be relayed to multiple LLMs, each returning its response. The system will collect these responses, compare them, and use various metrics—including similarity among responses, the historical accuracy of each LLM, and other statistical measures—to determine the most probable correct answer. This selected answer will then be presented to the user. The goal is to reduce the incidence of incorrect responses by utilizing the combined strength of multiple LLM models and assessing the reliability of their responses.

A main aspect of the project we will research and study is “How can multiple LLMs be effectively utilized to improve the accuracy and reliability of responses to user queries?”, where we will identify the strengths and limitations of each LLM by comparing their responses to a set of predefined questions. Also, we will develop an algorithm that evaluates the consistency and reliability of responses from different LLMs. In addition, we will study the possibility of using an LLM or multiple LLMs to read through all LLM's responses and give out the most common answer. Furthermore, we will come up with a methodology for evaluating the effectiveness of the combined LLM approach through manual testing and statistical analysis.

**Our implementation steps are as follows:**

1. Our first implementation step is to identify how to distinguish between answers of different LLMs to the same query, we will first conduct research to identify what data three of the LLMs have been trained on. Then we will manually curate and test a set of queries for comparison. After that, we will manually analyze the results from different LLMs, documenting the differences and potential inaccuracies. We will then score each answer from one to five using these criteria: accuracy, relevance, completeness. We will then manually evaluate the results using a scoring system as follows:   
     
   **Accuracy**: 5 \= fully correct,  
                           3 \= partially correct,  
                1 \= incorrect.  
     
   **Relevance:** 5 \= highly relevant,  
                               3 \= moderately relevant,  
               1 \= irrelevant.  
     
   **Completeness:** 5 \= Answer fully solved,  
                                    3 \= Answer Partially solved,  
                            1 \= Answer not solved.  
     
   This will help us track the performance of each LLM model on each question.  
     
2.  Then we will manually combine the answers based on the higher scores of each LLM response. After that, we will develop an algorithm that will automatically score the answers and combine them where we will research ways to score and combine the results.  
3. We will code a prototype file that will call the three LLMs, ask them questions and apply the algorithm we came up with from step 2 to combine or choose the right answer. Then we will manually test the answers using already prepared questions and using the scoring system. We will keep refining the algorithm and researching different algorithms until we get to a satisfactory result.  
4. We will gradually add three more LLMs, repeat step 3 for each addition, and continue this process until all the LLMs from a predefined list have been included.  
5.  The prototype will be evaluated by running queries and comparing the combined answers to see if the system improves accuracy compared to individual LLM responses. We will compare the combined responses to ground truth answers or human-evaluated responses to ensure the system is functioning as expected.  
6. Add extra functionality, where will let the LLM with the highest score to do compare the answers of multiple AIs and produce the optimal result. We will then evaluate this approach with the previous one to see wether this is more efficient, furthermore, we will try the same approach with different LLMs with the highest scores.  
7. We will create an interface in a webpage where user can interact with our system and ask questions and then get results.

***Division of Work***

The work will be divided equally between the two team members as follows:

**Ayoub Al-Kendi** will focus mainly on the back-end development, including integrating multiple LLMs, handling data flow between the models, and developing the algorithm for answer evaluation and selection. Also, will contribute to front-end development.

**Conor McQuillan** will focus more on front-end development, including creating the user interface for question input and result display and ensuring a smooth and intuitive user experience. Also, will contribute to back-end development.

Both members will collaborate on testing and refining the overall system, including conducting accuracy tests on LLM responses, gathering feedback, and improving the selection algorithm.

***Programming languages/Tools***

* Python to call LLMs APIs and write algorithms to compare and evaluate answers.  
* VS Code: For code development and version control.  
* Git: To manage version control and collaborative work.  
* APIs: OpenAI API, Gemini API, and more LLM APIs for LLM communication.  
* Node.js: To support back-end operations and API handling.  
* React.js: For developing a responsive and user-friendly front-end interface.  
* Postman: For testing and debugging API calls.


***Learning Challenges***

* Learning how to host the website online  
* Integrating Multiple LLMs: Learning to connect and handle multiple AI models through APIs effectively requires understanding different API specifications and optimizing request handling.  
* Algorithm Design: Developing an efficient and effective algorithm to compare and evaluate answers from different LLMs to produce the best response.  
* Front-End Development: Enhancing our skills in front-end frameworks like React.js, especially in building responsive and interactive components.  
* Handling LLMs Limitations: Understanding and mitigating the limitations of LLMs, such as response variability and potential bias.  
* Study and learn different evaluation techniques.


  
***Hardware/software platform*** 

* PCs running Windows or Linux.  
* Software: Windows Subshell for Linux

***Special Hardware / Software Requirements***

There are no special hardware requirements. All software tools will be open-source or accessible via standard developer subscriptions. The project will be developed and tested using standard lab machines or personal PCs, and the final demonstration will take place using the School of Computing lab facilities.

*TimeLine*   
*October:*

* Gather ideas for project proposal   
* Create a proposal/ present it   
* Conduct research on LLMs  
* Curate and select test queries.


*November* 

* Conduct manual analysis and comparison of LLM responses.  
* Manually compare and analyze the responses, scoring each based on criteria like accuracy and relevance and document the results.  
* Begin writing the Functional Specification.  
* 29th of November is submission of functional specification. 

*December*

* Begin designing and coding the algorithm for automatic scoring and comparison of LLM responses.  
* Research different techniques for scoring and combining LLM responses.  
* Begin coding the prototype that calls the LLMs, runs the queries, and applies the scoring algorithm.  
* Prepare for January's testing phase.

*January*

* Test the prototype system that applies the scoring and comparison algorithm to the LLMs.  
* Refine the algorithm based on the results and ensure it functions accurately.  
* Identify discrepancies between the prototype's output and manual scores, focusing on areas like accuracy, relevance, and completeness.  
* Re-run the tests to ensure the refined algorithm produces better results.  
* Integrate additional LLMs into the system.  
* Test the system with the newly added LLMs, running the same set of queries and using the refined algorithm to score and combine answers.  
* Compare results from the expanded set of LLMs to ensure that the system scales effectively and still produces accurate and relevant responses.  
* Create a User interface for the system.

*February*

* Conduct a final round of testing, ensuring that the system is functioning as intended with all integrated LLMs.  
* Finalize the algorithm based on the results of the expanded testing.  
* Complete all project documentation, including any required functional specifications, technical details, and the user manual.  
* Prepare for and deliver the project demonstrations.

