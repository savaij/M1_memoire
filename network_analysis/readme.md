# Workflow pipeline network analysis:
- create network from two different incel groups
- create network from far-right groups
- create network from far-left groups as "control group"

- check connections between the networks to grasp the influence of communication between far right groups and incel ones

<br><br>

# Content

- `number_nodes.ipynb`: code used to compare the number of nodes in each network and calculate its z-score (memoire section 2.2)

- `comparison_degree.ipynb`: code used to calculate “node degree overlap” (Sections 3.1 and 4.1)

- `comparison_communities_separation.ipynb`: code used to calculate "community separation" (Sections 3.2 and 4.2)

- `forward_module`: python module created to scrape messages and forwards. They are used in the edgelists' notebooks.

<br>

In each of the folders there are code and data of the network. Each network is created through a snowball sampling iterated three times. Each network folder follows this pattern:

- `notebooks`: folder with the code used to create the network

    - `first_edgelist.ipynb`: scrape data from the first two groups chosen as origin of the network. Get all messages forwarded from other groups and get the ID of the group.
    
        Data are stored in `first_edgelist` folder in a csv in this format:

        If some messages received on group A are forwarded from group B:

        | forward_from | forward_to | count |
        |--------------|------------|-------|
        | id_group_B   | id_group_A | 290   |

        Where: <br>
        • id_group_A and id_group_B are numerical IDs of A and B

        • 290 is the number of messages forwarded from group B to group A
        <br><br>
    
    - the same pattern is followed for second and third edgelists (e.i. at the second and third iteration of the sampling)


- `dictionaires`: file json to link groups' IDs to groups' names and descriptions


<br><br>

Files with private credentials to access the Telegram API were not included