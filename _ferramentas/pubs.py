# Bibliografia de Telma Woerle de Lima Soares.
# Fonte da lista: registro DBLP dela (espelhado em csauthors.net), que aponta para o Lattes 6296363436468330
# e o ORCID 0000-0002-4927-2221. Links "verificados" foram abertos; os demais levam à busca do título no DBLP.
from urllib.parse import quote
J, C, P = ("Artigo em periódico", "Journal article"), ("Artigo em conferência", "Conference paper"), ("Preprint", "Preprint")
V = {  # links conferidos na fonte
 "Sliding Puzzles Gym: A Scalable Benchmark for State Representation in Visual Reinforcement Learning": "https://proceedings.mlr.press/v267/de-oliveira25a.html",
 "Partial Reasoning in Language Models: Search and Refinement Guided by Uncertainty": "https://arxiv.org/abs/2601.12040",
 "Learning Without Critics? Revisiting GRPO in Classical Reinforcement Learning Environments": "https://arxiv.org/abs/2511.03527",
}
R = [
 (2026, P, "arXiv", "Do Reasoning Models Ask Better Questions? A Formal Information-Theoretic Analysis on Multi-Turn LLM Games", "Daniel M. Pedrozo, Bryan L. M. de Oliveira"),
 (2026, C, "LaCATODA Workshop 2026", "Partial Reasoning in Language Models: Search and Refinement Guided by Uncertainty", "Murilo Lopes da Luz, Bruno Brandão, Luana G. B. Martins, Gustavo Oliveira, Bryan L. M. de Oliveira, Luckeciano Carvalho Melo"),
 (2025, P, "arXiv", "Learning Without Critics? Revisiting GRPO in Classical Reinforcement Learning Environments", "Bryan L. M. de Oliveira, Felipe Vieira Frujeri, Marcos P. C. M. Queiroz, Luana G. B. Martins, Luckeciano C. Melo"),
 (2025, C, "SIBGRAPI 2025", "Automated Synthetic Data for Computer Vision: Blender-COCO Pipeline Enhancing Yolov8", "Victor Roza Souza, Djonathan Caua Fritzen Christ, Igor Scaliante Wiese, Thiago França Naves, Anderson da Silva Soares, Luciana de Oliveira Berretta"),
 (2025, C, "SBSI 2025", "Enhancing NeRFs for High-Quality Indoor Video Generation: A Study on Parameterization and Recording Methods", "Tafnes Silva Barbosa, Luis Henrique da S. Resende, Iuri Almeida Pereira, Igor Scaliante Wiese, Thiago França Naves, Anderson da Silva Soares"),
 (2025, C, "ICML 2025", "Sliding Puzzles Gym: A Scalable Benchmark for State Representation in Visual Reinforcement Learning", "Bryan Lincoln Marques de Oliveira, Luana Guedes Barros Martins, Bruno Brandão, Murilo Lopes da Luz, Luckeciano Carvalho Melo"),
 (2024, J, "Sensors", "Deep Deterministic Policy Gradient-Based Resource Allocation Considering Network Slicing and Device-to-Device Communication in Mobile Networks", "Hudson Henrique De Souza Lopes, Lucas Jose Ferreira Lima, Flávio Henrique Teles Vieira"),
 (2024, C, "SVR 2024", "Fine-Tuning a Video Masked Autoencoder to Develop an Augmented Reality Application for Brazilian Sign Language Interpretation", "Rodrigo Zempulski Fanucchi, Arlindo Rodrigues Galvão Junior, Gabriel da Mata Marques, Lucas Brandão Rodrigues, Anderson da Silva Soares"),
 (2022, J, "IEEE Access", "Multiagent Reinforcement Learning for Strategic Decision Making and Control in Robotic Soccer Through Self-Play", "Bruno Brandão, Anderson Soares, Luckeciano C. Melo, Marcos R. O. A. Máximo"),
 (2022, C, "Intelligent Systems and Applications 2022", "A Hybrid Predictor for Protein Tertiary Structures", "Alexandre Almeida"),
 (2020, C, "PPSN XVI", "On Sharing Information Between Sub-populations in MOEA/S", "Lucas de Almeida Ribeiro, Michael Emmerich, Anderson da Silva Soares"),
 (2020, C, "GECCO 2020", "New search operators for node-depth based encoding", "Gustavo Post Sabin, Anderson da Silva Soares"),
 (2019, J, "Engineering Applications of Artificial Intelligence", "Epistasis-based FSA: Two versions of a novel approach for variable selection in multivariate calibration", "Lauro C. M. de Paula, Anderson da Silva Soares, Celso G. Camilo-Junior, Clarimar José Coelho, Anselmo E. de Oliveira"),
 (2019, C, "IEEE ICTAI 2019", "Generating Reduced Tests for FSMs using a Search-Based Testing Approach", "Mariana Soller Ramada, Anderson da Silva Soares, Adenilso Simão"),
 (2017, J, "Journal of Computer Science", "Modern Metaheuristic with Multi-Objective Formulation for the Variable Selection Problem", "Lauro Cássio Martins de Paula, Anderson da Silva Soares, Anselmo E. de Oliveira, Clarimar José Coelho"),
 (2017, J, "Computing", "Parallel regressions for variable selection using GPU", "Lauro Cássio Martins de Paula, Anderson da Silva Soares, Arlindo R. G. Filho, Clarimar José Coelho, Alexandre C. B. Delbem, Wellington Santos Martins"),
 (2017, C, "GECCO 2017", "Variable selection as a non-completely decomposable problem: a case study in multivariate calibration", "Lauro C. M. de Paula, Anderson da Silva Soares, Clarimar José Coelho"),
 (2017, C, "Progress in Artificial Intelligence (EPIA) 2017", "A Stochastic Approach of SIRC Model Using Individual-Based Epidemiological Models", "Arlindo Rodrigues Galvão Filho, Anderson da Silva Soares, Clarimar José Coelho"),
 (2017, C, "IEEE CEC 2017", "Integer-based genetic algorithm for feature selection in multivariate calibration", "Rhelcris S. Sousa, Lauro C. M. de Paula, Roney Lopes Lima, Arlindo R. G. Filho, Anderson da Silva Soares"),
 (2016, J, "Swarm and Evolutionary Computation", "Node-depth phylogenetic-based encoding, a spanning-tree representation for evolutionary algorithms. Part I: Proposal and properties analysis", "Alexandre Cláudio Botazzo Delbem, Anderson da Silva Soares, Fernando Marques Federson, João Bosco Augusto London Junior, Jeffrey Van Baalen"),
 (2016, J, "Computers and Electronics in Agriculture", "A feasibility cachaca type recognition using computer vision and pattern recognition", "Bruno Urbano Rodrigues, Anderson da Silva Soares, Ronaldo Martins da Costa, Jeffrey Van Baalen, Rogerio Lopes Salvini, F. A. Silva, Márcio Caliari, Karla Cristina Rodrigues Cardoso, Tânia Isabel Monteiro Ribeiro, Alexandre C. B. Delbem, Fernando Marques Federson, Clarimar José Coelho, Gustavo Teodoro Laureano"),
 (2016, C, "ICCS 2016", "An Evolutionary Algorithm for Autonomous Robot Navigation", "Anderson da Silva Soares"),
 (2016, C, "ICCS 2016", "Permutation-based Recombination Operator to Node-depth Encoding", "Alexandre C. B. Delbem, Roney Lopes Lima, Gustavo Post Sabin, Marcos Antônio Almeida de Oliveira"),
 (2016, C, "GECCO 2016", "Variable Selection for Multivariate Calibration in Chemometrics: A Real-World Application with Building Blocks Disruption Problem", "Lauro C. M. de Paula, Anderson da Silva Soares, Arlindo R. G. Filho, Clarimar José Coelho"),
 (2016, C, "GECCO 2016", "Feature Selection using Genetic Algorithm: An Analysis of the Bias-Property for One-Point Crossover", "Lauro C. M. de Paula, Anderson da Silva Soares, Clarimar José Coelho"),
 (2016, C, "IEEE CEC 2016", "A compact firefly algorithm for the variable selection problem in pharmaceutical ingredient determination", "Lauro C. M. de Paula, Heber V. Nogueira, Anderson da Silva Soares, Clarimar José Coelho"),
 (2015, J, "Journal of Computer Science", "Genetic Algorithm for Variable and Samples Selection in Multivariate Calibration Problems", "Kelton de Souza Santiago, Anderson da Silva Soares, Clarimar José Coelho, Paulo Henrique Ribeiro Gabriel"),
 (2015, C, "ICCS 2015", "Multi-objective Genetic Algorithm for Variable Selection in Multivariate Classification Problems: A Case Study in Verification of Biodiesel Adulteration", "Lucas de Almeida Ribeiro, Anderson da Silva Soares, Carlos Antônio Campos Jorge, Ronaldo Martins da Costa, Rogerio Lopes Salvini, Clarimar José Coelho, Fernando Marques Federson, Paulo Henrique Ribeiro Gabriel"),
 (2015, C, "EMO 2015", "Multi-objective Evolutionary Algorithm with Discrete Differential Mutation Operator for Service Restoration in Large-Scale Distribution Systems", "Danilo Sipoli Sanches, João Bosco A. London Jr., Alexandre Cláudio Botazzo Delbem, Ricardo S. Prado, Frederico G. Guimarães"),
 (2014, J, "International Journal of Natural Computing Research", "Parallelization of a Modified Firefly Algorithm using GPU for Variable Selection in a Multivariate Calibration Problem", "Lauro C. M. de Paula, Anderson da Silva Soares, Alexandre C. B. Delbem, Clarimar José Coelho, Arlindo Rodrigues Galvão Filho"),
 (2013, C, "ICAISC 2013", "Hybrid Genetic-Fuzzy Algorithm for Variable Selection in Spectroscopy", "Anderson da Silva Soares, Clarimar José Coelho, Rogerio Salvini, Gustavo Teodoro Laureano"),
 (2013, C, "IEEE CEC 2013", "Multi-objective evolutionary algorithm for variable selection in calibration problems: A case study for protein concentration prediction", "Daniel Vitor de Lucena, Anderson da Silva Soares, Alexandre C. B. Delbem, Arlindo Rodrigues Galvão Filho, Clarimar José Coelho, Gustavo Teodoro Laureano"),
 (2012, J, "IEEE Transactions on Evolutionary Computation", "Efficient Forest Data Structure for Evolutionary Algorithms Applied to Network Design", "Alexandre C. B. Delbem, Guilherme P. Telles"),
 (2012, J, "International Journal of Natural Computing Research", "Multi-Objective Evolutionary Algorithm NSGA-II for Variables Selection in Multivariate Calibration Problems", "Daniel Vitor de Lucena, Anderson da Silva Soares, Clarimar José Coelho"),
 (2011, C, "GECCO 2011", "Analysis of properties of recombination operators proposed for the node-depth encoding", "Alexandre Cláudio Botazzo Delbem, Franz Rothlauf"),
 (2008, C, "GECCO 2008", "The node-depth encoding: analysis and application to the bounded-diameter minimum spanning tree problem", "Franz Rothlauf, Alexandre C. B. Delbem"),
 (2007, C, "GECCO 2007", "Evolutionary approach to protein structure prediction with hydrophobic interactions", "Rodrigo Antonio Faccioli, Paulo Henrique Ribeiro Gabriel, Alexandre C. B. Delbem, Ivan Nunes da Silva"),
 (2007, C, "IEEE CEC 2007", "Evolutionary algorithm to ab initio protein structure prediction with hydrophobic interactions", "Paulo Henrique Ribeiro Gabriel, Alexandre C. B. Delbem, Rodrigo Antonio Faccioli, Ivan Nunes da Silva"),
 (2005, C, "IEA/AIE 2005", "Node-Depth Encoding for Evolutionary Algorithms Applied to Multi-vehicle Routing Problem", "Giampaolo L. Libralao, Fabio C. Pereira, Alexandre C. B. Delbem"),
 (2005, C, "IEEE CEC 2005", "Node-depth encoding for directed graphs", "Giampaolo L. Libralao, Karen Honda, Alexandre C. B. Delbem"),
]
def lista():
    out = []
    for ano, tp, vei, tit, co in R:
        ver = tit in V
        out.append({"ano": ano, "tipo": tp[0], "tipo_en": tp[1], "veiculo": vei, "titulo": tit, "coautores": co,
                    "url": V.get(tit) or "https://dblp.org/search?q=" + quote(tit), "link_verificado": ver})
    out.append({"ano": 2009, "tipo": "Tese de doutorado", "tipo_en": "Doctoral thesis", "veiculo": "USP", "titulo": "Estruturas de dados eficientes para algoritmos evolutivos aplicados a projeto de redes", "coautores": "", "url": "https://teses.usp.br/teses/disponiveis/55/55134/tde-28052009-163303/pt-br.html", "link_verificado": True})
    out.append({"ano": 2006, "tipo": "Dissertação de mestrado", "tipo_en": "Master's dissertation", "veiculo": "USP", "titulo": "Algoritmos evolutivos para predição de estruturas de proteínas", "coautores": "", "url": "https://teses.usp.br/teses/disponiveis/55/55134/tde-30092006-110850/pt-br.html", "link_verificado": True})
    out.sort(key=lambda p: -p["ano"])
    return out
