'Brain of Life' is an modified version of the famous cellular automata Conway's Game of Life designed to visualize the workings of the human brain through a neural network and abstracted brain mapping, while preserving the radical simplicity and adaptability of the original game.

##Inspiration
With the uprising popularity of neural network models and newer applications of artificial intelligence inspired by the human brain, our team thought it as necessary for the average technology user to have a good understanding of the logical origin of these models. This prompted us to develop a highly abstracted brain mapping program in which the user can design their own 'brain stems' in a circuit-like simulation with the use of 5 cell states: power source, firing neuron, resting neuron, connectors, and dead. With just these 5 stats and a very simple set of rules, the user is able to develop a visual understanding of the process of reinforced learning and the origin of neural networks as a concept.

##What it does
Our project allows for the user to play with the different status types and for them to build a circuit-like simulation of the exemplified human brain.

##How we built it
Through the use of the pygame library, we were able to create a clickable grid that colors in the cells based on the user's choice of state and their design. As the grid draws the input, the python code is registering the individual coordinates of each input and categorizing them by state in a matrix, allowing us to be able to pull the coordinates directly and to carefully design how the cells interact with each other.

Through the use of numpy, our team's neural network implementation consists of constructing the power cell to predict clusters of 'nerve endings' by using the different areas of the brain, a simple plain vanilla neural network structure, the Sigmoid function for readability, as well as basic biological concepts of the brains functioning and taking inspiration from concepts of neuroscience.

##Challenges we ran into
It was difficult finding the appropriate libraries and methods to get our idea through, but after thorough thinking, we came to the conclusion that a simple approach would bring a better understanding for the user, and it would also enrich our learning the most.

##Accomplishments that we're proud of
We are immensely proud of the amount of work that we were able to accomplish in such a short amount of time, as well as realizing our ambitions as a team and being able to handle so many concepts and topics that we were not familiar with beforehand.

##What we learned
Besides effective task designation, good communication, and role keeping to maintain efficiency, our team acquired a complete and complex understanding of the working of plain vanilla neural networks, we also had to learn object-oriented programming principles in order to create an efficient and powerful system, and we also learnt how to utilize pygame and to curate tools for the best user experience possible.

##What's next for Brain of Life
We hope that we get to eventually fully implement all of the initial ideas and tools that we had in mind for the project.
