#### Group 4
#### Use Case for Quality Assessment

### Title
Quality Assessment

#### Description
This use case describes the quality classification of images process. The actors are the photographer and editors. The photographer will input an image or set of images into the system with appropriate metadata. When ready, the machine will attempt to provide a quality ranking (1-10) to each of the pictures. The editor will be used to guarantee the rankings are accurate.   

#### Triggers
1. Photographer uploads pictures to system.
2. Editor re-runs classification process on picture.

#### Actors
* Photographer
* Editor

#### Preconditions
1. The classifier has been appropriately trained.
2. The photographer submits a valid photograph format.

#### Main Success Scenario (Goals)
1. The classifier correctly assigns a quality rank to each of the photographs on the supplied set and adds the rank and appropriate tags to the metadata.

#### Alternate Success Scenarios
1. The classifier assigns a rank the editor disagrees with.
2. The classifier assigns a rank but includes no tags.

#### Failed End Condition
1. The classifier fails to assign a rank to the set of photographs.
2. The classifier only assigns a rank to one photograph given a set.

#### Extensions
1. The classifier assigns a rank the editor disagrees with.
    1.  Editor submits new rank to system.
    2.  Algorithm makes adjustment based on new data.
    3.  New rank is stored in picture metadata instead.
2. The classifier assigns a rank but includes no tags.
    1.  Rank is assigned and photo is stored without tags.
    2.  Noted in error log with unique picture ID.

#### Steps of Execution (Requirements)
1.  The photographer submits a one or many photographs to the classifier.
2.  The classifier runs on each of the photographs and assigns a rank and adds tags.
3.  When finished, the classifier pulls a random number of low, medium, and high ranked photographs (no more then 10) and asks the editor to review the ranks. 
    1.  If editor is unsatisfied, retrain
4. Store photographs and metadata.

#### Use Case Diagram
![load data](https://github.com/MJC598/RJI-Software-Engineering-Project/blob/master/diagrams/quality_assessment.png "quality_assessment_diagram")

Created By: Matthew Carroll

Reviewed By:

Collaborated With:
