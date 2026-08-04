
# RecSys NRT - recsys_data_prep updates

We will still have a daily job to get data that could have been updated without us knowing. This is basically any column that the webhook does not fire on when it updates.

We will still get a daily csv dump from database with stale data. We can grab the set of ids in the active listings and the at ef files and compare that set of ids to the set of ids within es, anything within ES that is not in the file is a delete, anything within the file that is not es is an add. Ids that are in both are potentially an update. To combat the potential uncertainty we will add a recsysLastModified datetime column, anything with a lastModifedDate of less than 24 hours we will assume is current, anything out side of that will be added to the set of ids to be processed.

Once that set of ids is found we will need to write those ids to a pulsar topic for the NRT pipeline to process. These should have a lower priority than true NRT updates from the webhook.

