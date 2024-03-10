package sample;

import javafx.event.ActionEvent;
import javafx.fxml.Initializable;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;

import java.io.*;
import java.net.URL;
import java.util.ResourceBundle;

public class Controller implements Initializable {
    //reminder
    public ListView<Reminder> reminderList;
    public TextField getReminderTitle;
    public TextField getReminderDueDate;
    public TextField getReminderDescrip;
    public Label lblReminderTitle;
    public Label lblReminderDueDate;
    public Label lblReminderDescrip;
    public ListView loadReminderGroups;
    public TextField groupName;
    String line;
    int lineNum = 0;
    String loadReminderTitle;
    String loadReminderDueDate;
    String loadReminderDescrip;

    //event
    public ListView<Event> eventList;
    public TextField getEventTitle;
    public TextField getEventLocation;
    public TextField getEventDate;
    public TextField getEventDescrip;
    public Label lblEventTitle;
    public Label lblEventLocation;
    public Label lblEventDate;
    public Label lblEventDescrip;
    public ListView loadEventGroups;
    public TextField eventGroupName;
    String line2;
    int lineNum2 = 0;
    String loadEventTitle;
    String loadEventLocation;
    String loadEventDate;
    String loadEventDescrip;

    //goal
    public ListView<Goal> goalList;
    public TextField getGoalTitle;
    public TextField getGoalDueDate;
    public TextField getGoalDescrip;
    public Label lblGoalTitle;
    public Label lblGoalDueDate;
    public Label lblGoalDescrip;
    public ListView loadGoalGroups;
    public TextField goalGroupName;
    String line3;
    int lineNum3 = 0;
    String loadGoalTitle;
    String loadGoalDueDate;
    String loadGoalDescrip;


    FileReader fr = new FileReader("reminderInfo.txt");
    BufferedReader br = new BufferedReader(fr);

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        try {
            //for each line in the buffer reader
            while ((line = br.readLine()) != null) {
                lineNum++;
                //first line
                if (lineNum % 3 == 1){
                    loadReminderTitle = line;
                }
                //second line
                else if (lineNum % 3 == 2){
                    loadReminderDueDate = line;
                }
                //third line
                else if (lineNum % 3 == 0){
                    loadReminderDescrip = line;
                    //create new reminder and add to reminder list
                    Reminder reminder = new Reminder(loadReminderTitle, loadReminderDueDate, loadEventDescrip);
                    reminderList.getItems().add(reminder);
                }
            }
            //close file
            br.close();
            //open reminderGroups file
            FileReader frB = new FileReader("reminderGroups.txt");
            BufferedReader brB = new BufferedReader(frB);
            //for each line in the file
            while((line = brB.readLine()) != null){
                //add new group
                loadReminderGroups.getItems().add(line);
            }
            //close file
            brB.close();
        }catch(IOException e){
            //print to trace if anything goes wrong
            e.printStackTrace();
        }

        try {
            //for each line in the buffer reader
            while ((line2 = br2.readLine()) != null) {
                lineNum2++;
                //first line
                if (lineNum2 % 4 == 1){
                    loadEventTitle = line2;
                }
                //second line
                else if (lineNum2 % 4 == 2){
                    loadEventLocation = line2;
                }
                //third line
                else if (lineNum2 % 4 == 3){
                    loadEventDate = line2;
                }
                //fourth line
                else if (lineNum2 % 4 == 0){
                    loadEventDescrip = line2;
                    //create new event and add to event list
                    Event event = new Event(loadEventTitle, loadEventLocation, loadEventDate, loadEventDescrip);
                    eventList.getItems().add(event);
                }
            }
            //close file
            br2.close();
            //open eventGroups file
            FileReader frC = new FileReader("eventGroups.txt");
            BufferedReader brC = new BufferedReader(frC);
            //for each line in the file
            while((line2 = brC.readLine()) != null){
                //add new group
                loadEventGroups.getItems().add(line2);
            }
            //close file
            brC.close();
        }catch(IOException e){
            //print to trace if anything goes wrong
            e.printStackTrace();
        }

        try {
            //for each line in the buffer reader
            while ((line3 = br3.readLine()) != null) {
                lineNum3++;
                //first line
                if (lineNum3 % 3 == 1){
                    loadGoalTitle = line3;
                }
                //second line
                else if (lineNum3 % 3 == 2){
                    loadGoalDueDate = line3;
                }
                //third line
                else if (lineNum3 % 3 == 0){
                    loadGoalDescrip = line3;
                    //create new goal and add to goal list
                    Goal goal = new Goal(loadGoalTitle, loadGoalDueDate, loadGoalDescrip);
                    goalList.getItems().add(goal);
                }

            }
            //close file
            br3.close();
            //open goalsGroups file
            FileReader frD = new FileReader("goalGroups.txt");
            BufferedReader brD = new BufferedReader(frD);
            //for each line in the file
            while((line3 = brD.readLine()) != null){
                //add new group
                loadGoalGroups.getItems().add(line3);
            }
            //close file
            brD.close();
        }catch(IOException e){
            //print to trace if anything goes wrong
            e.printStackTrace();
        }
    }
    public Controller() throws IOException {
    }

    public void viewRemindersGroup(ActionEvent actionEvent) throws IOException {
        //clear list
        reminderList.getItems().clear();
        //open new reminder group file based on selection
        FileReader fr = new FileReader(loadReminderGroups.getSelectionModel().getSelectedItem() + ".txt");
        BufferedReader br = new BufferedReader(fr);
        lineNum =0;
        //for each line in the file
        while ((line = br.readLine()) != null) {
            lineNum++;
            //first line
            if (lineNum % 3 == 1){
                loadReminderTitle = line;
            }
            //second line
            else if (lineNum % 3 == 2){
                loadReminderDueDate = line;
            }
            //third line
            else if (lineNum % 3 == 0){
                loadReminderDescrip = line;
                //create new reminder and add to reminder list
                Reminder reminder = new Reminder(loadReminderTitle, loadReminderDueDate, loadReminderDescrip);
                reminderList.getItems().add(reminder);
            }
        }
        //close file
        br.close();
    }
    public void viewAllRemindersList(ActionEvent actionEvent) throws IOException {
        //clear list
        reminderList.getItems().clear();
        //open reminder info file
        FileReader fr = new FileReader("reminderInfo.txt");
        BufferedReader br = new BufferedReader(fr);
        //for each line in the file
        while ((line = br.readLine()) != null) {
            lineNum++;
            //first line
            if (lineNum % 3 == 1){
                loadReminderTitle = line;
            }
            //second line
            else if (lineNum % 3 == 2){
                loadReminderDueDate = line;
            }
            //third line
            else if (lineNum % 3 == 0){
                loadReminderDescrip = line;
                //create new reminder and add to reminder list
                Reminder reminder = new Reminder(loadReminderTitle, loadReminderDueDate, loadReminderDescrip);
                reminderList.getItems().add(reminder);
            }
        }
        //close file
        br.close();
    }
    public void newReminderGroup(ActionEvent actionEvent) throws IOException {
        //open new text file to append to
        FileWriter fw = new FileWriter(groupName.getText() + ".txt", true);
        //add new group to list
        loadReminderGroups.getItems().add(groupName.getText());
        //open reminderGroups file to append to
        FileWriter fwB = new FileWriter("reminderGroups.txt", true);
        //write to file
        BufferedWriter bwB = new BufferedWriter(fwB);
        bwB.write(groupName.getText() + "\n");
        //close buffered writer
        bwB.close();
        groupName.clear();
    }
    public void addReminderToGroup(ActionEvent actionEvent) throws IOException {
        //get currently selected reminder from list
        Reminder temp;
        temp = reminderList.getSelectionModel().getSelectedItem();
        //open new reminder group file based on selection
        FileWriter fw = new FileWriter(loadReminderGroups.getSelectionModel().getSelectedItem()+ ".txt", true);
        //write to file
        BufferedWriter bw = new BufferedWriter(fw);
        //write reminder title, due date, and description on 3 different lines
        bw.write(temp.getReminderTitle() + "\n" + temp.getReminderDueDate() + "\n" + temp.getReminderDescrip() + "\n" );
        //close buffered writer
        bw.close();
    }
    public void addReminder(ActionEvent actionEvent) throws IOException {
        //current reminder to add to list
        Reminder temp = new Reminder(getReminderTitle.getText(), getReminderDueDate.getText(), getReminderDescrip.getText());
        //open reminderInfo file to append to
        FileWriter fw = new FileWriter("reminderInfo.txt", true);
        //write to file
        BufferedWriter bw = new BufferedWriter(fw);
        //write reminder title, due date, and description on 3 different lines
        bw.write(getReminderTitle.getText() + "\n" + getReminderDueDate.getText() + "\n" + getReminderDescrip.getText() + "\n");
        //close buffered writer
        bw.close();
        //add to reminder list
        reminderList.getItems().add(temp);
        //clear reminder title, due date, and description text field
        getReminderTitle.clear();
        getReminderDueDate.clear();
        getReminderDescrip.clear();
    }
    public void deleteReminder(ActionEvent actionEvent) {
        //remove selected reminder from reminder list
        reminderList.getItems().remove(reminderList.getSelectionModel().getSelectedItem());
        //clear reminder title, due date, and description label
        lblReminderTitle.setText("Reminder Title:");
        lblReminderDueDate.setText("Due Date:");
        lblReminderDescrip.setText("Description:");
    }
    public void displayReminder(MouseEvent mouseEvent) {
        //get currently selected reminder from list
        Reminder temp;
        temp = reminderList.getSelectionModel().getSelectedItem();
        //set and display reminder title, due date, and description label
        lblReminderTitle.setText("Reminder Title: " + temp.getReminderTitle());
        lblReminderDueDate.setText("Due Date: " + temp.getReminderDueDate());
        lblReminderDescrip.setText("Description: " + temp.getReminderDescrip());
    }


    FileReader fr2 = new FileReader("eventInfo.txt");
    BufferedReader br2 = new BufferedReader(fr2);

    public void viewEventGroup(ActionEvent actionEvent) throws IOException {
        //clear list
        eventList.getItems().clear();
        //open new event group file based on selection
        FileReader fr3 = new FileReader(loadEventGroups.getSelectionModel().getSelectedItem() + ".txt");
        BufferedReader br3 = new BufferedReader(fr3);
        lineNum2 = 0;
        //for each line in the file
        while ((line2 = br3.readLine()) != null) {
            lineNum2++;
            //first line
            if (lineNum2 % 4 == 1){
                loadEventTitle = line2;
            }
            //second line
            else if (lineNum2 % 4 == 2){
                loadEventLocation = line2;
            }
            //third line
            else if (lineNum2 % 4 == 3){
                loadEventDate = line2;
            }
            //fourth line
            else if (lineNum2 % 4 == 0){
                loadEventDescrip = line2;
                //create new event and add to event list
                Event event = new Event(loadEventTitle, loadEventLocation, loadEventDate, loadEventDescrip);
                eventList.getItems().add(event);
            }
        }
        //close file
        br3.close();
    }
    public void viewAllEventsList(ActionEvent actionEvent) throws IOException {
        //clear list
        eventList.getItems().clear();
        //open event info file
        FileReader fr4 = new FileReader("eventInfo.txt");
        BufferedReader br4 = new BufferedReader(fr4);
        //for each line in the file
        while ((line2 = br4.readLine()) != null) {
            lineNum2++;
            //first line
            if (lineNum2 % 4 == 1){
                loadEventTitle = line2;
            }
            //second line
            else if (lineNum2 % 4 == 2){
                loadEventLocation = line2;
            }
            //third line
            else if (lineNum2 % 4 == 3){
                loadEventDate = line2;
            }
            //fourth line
            else if (lineNum2 % 4 == 0){
                loadEventDescrip = line2;
                //create new event and add to event list
                Event event = new Event(loadEventTitle, loadEventLocation, loadEventDate, loadEventDescrip);
                eventList.getItems().add(event);
            }
        }
        //close file
        br4.close();
    }
    public void newEventGroup(ActionEvent actionEvent) throws IOException {
        //open new text file to append to
        FileWriter fw2 = new FileWriter(eventGroupName.getText() + ".txt", true);
        //add new group to list
        loadEventGroups.getItems().add(eventGroupName.getText());
        //open eventsGroups file to append to
        FileWriter fwC = new FileWriter("eventGroups.txt", true);
        //write to file
        BufferedWriter bwC = new BufferedWriter(fwC);
        bwC.write(eventGroupName.getText() + "\n");
        //close buffered writer
        bwC.close();
        eventGroupName.clear();
    }
    public void addEventToGroup(ActionEvent actionEvent) throws IOException {
        //get currently selected event from list
        Event temp;
        temp = eventList.getSelectionModel().getSelectedItem();
        //open new event group file based on selection
        FileWriter fw2 = new FileWriter(loadEventGroups.getSelectionModel().getSelectedItem()+ ".txt", true);
        //write to file
        BufferedWriter bw2 = new BufferedWriter(fw2);
        //write event title, location, date, and description on 4 different lines
        bw2.write(temp.getEventTitle() + "\n" + temp.getEventLocation() + "\n" + temp.getEventDate() + "\n" + temp.getEventDescription() + "\n" );
        //close buffered writer
        bw2.close();
    }
    public void addEvent(ActionEvent actionEvent) throws IOException {
        //current event to add to list
        Event temp = new Event(getEventTitle.getText(), getEventLocation.getText(), getEventDate.getText(), getEventDescrip.getText());
        //open eventInfo file to append to
        FileWriter fw2 = new FileWriter("eventInfo.txt", true);
        //write to file
        BufferedWriter bw2 = new BufferedWriter(fw2);
        //write event title, location, date, and description on 4 different lines
        bw2.write(getEventTitle.getText() + "\n" + getEventLocation.getText() + "\n" + getEventDate.getText() + "\n" + getEventDescrip.getText() + "\n" );
        //close buffered writer
        bw2.close();
        //add to event list
        eventList.getItems().add(temp);
        //clear event title, location, date, and description text field
        getEventTitle.clear();
        getEventLocation.clear();
        getEventDate.clear();
        getEventDescrip.clear();
    }
    public void deleteEvent(ActionEvent actionEvent) {
        //remove selected event from event list
        eventList.getItems().remove(eventList.getSelectionModel().getSelectedItem());
        //clear event title, location, date, and description label
        lblEventTitle.setText("Event Title:");
        lblEventLocation.setText("Location:");
        lblEventDate.setText("Date:");
        lblEventDescrip.setText("Description:");
    }
    public void displayEvent(MouseEvent mouseEvent) {
        //get currently selected event from list
        Event temp;
        temp = eventList.getSelectionModel().getSelectedItem();
        //set and display event title, location, date, and description label
        lblEventTitle.setText("Event Title: " + temp.getEventTitle());
        lblEventLocation.setText("Location: " + temp.getEventLocation());
        lblEventDate.setText("Date: " + temp.getEventDate());
        lblEventDescrip.setText("Description: " + temp.getEventDescription());
    }


    FileReader fr3 = new FileReader("goalInfo.txt");
    BufferedReader br3 = new BufferedReader(fr3);

    public void viewGoalGroup(ActionEvent actionEvent) throws IOException {
        //clear list
        goalList.getItems().clear();
        //open new goal group file based on selection
        FileReader fr4 = new FileReader(loadGoalGroups.getSelectionModel().getSelectedItem() + ".txt");
        BufferedReader br4 = new BufferedReader(fr4);
        lineNum3 =0;
        //for each line in the file
        while ((line3 = br4.readLine()) != null) {
            lineNum3++;
            //first line
            if (lineNum3 % 3 == 1){
                loadGoalTitle = line3;
            }
            //second line
            else if (lineNum3 % 3 == 2){
                loadGoalDueDate = line3;
            }
            //third line
            else if (lineNum3 % 3 == 0){
                loadGoalDescrip = line3;
                //create new goal and add to goal list
                Goal goal = new Goal(loadGoalTitle, loadGoalDueDate, loadGoalDescrip);
                goalList.getItems().add(goal);
            }
        }
        //close file
        br4.close();
    }
    public void viewAllGoalsList(ActionEvent actionEvent) throws IOException {
        //clear list
        goalList.getItems().clear();
        //open goal info file
        FileReader fr4 = new FileReader("goalInfo.txt");
        BufferedReader br4 = new BufferedReader(fr4);
        //for each line in the file
        while ((line3 = br4.readLine()) != null) {
            lineNum3++;
            //first line
            if (lineNum3 % 3 == 1){
                loadGoalTitle = line3;
            }
            //second line
            else if (lineNum3 % 3 == 2){
                loadGoalDueDate = line3;
            }
            //third line
            else if (lineNum3 % 3 == 0){
                loadGoalDescrip = line3;
                //create new goal and add to goal list
                Goal goal = new Goal(loadGoalTitle, loadGoalDueDate, loadGoalDescrip);
                goalList.getItems().add(goal);
            }
        }
        //close file
        br4.close();
    }
    public void newGoalGroup(ActionEvent actionEvent) throws IOException {
        //open new text file to append to
        FileWriter fw4 = new FileWriter(goalGroupName.getText() + ".txt", true);
        //add new group to list
        loadGoalGroups.getItems().add(goalGroupName.getText());
        //open goalGroups file to append to
        FileWriter fwE = new FileWriter("goalGroups.txt", true);
        //write to file
        BufferedWriter bwE = new BufferedWriter(fwE);
        bwE.write(goalGroupName.getText() + "\n");
        //close buffered writer
        bwE.close();
        goalGroupName.clear();
    }
    public void addGoalToGroup(ActionEvent actionEvent) throws IOException {
        //get currently selected goal from list
        Goal temp;
        temp = goalList.getSelectionModel().getSelectedItem();
        //open new goal group file based on selection
        FileWriter fw4 = new FileWriter(loadGoalGroups.getSelectionModel().getSelectedItem()+ ".txt", true);
        //write to file
        BufferedWriter bw4 = new BufferedWriter(fw4);
        //write goal title, due date, and description on 3 different lines
        bw4.write(temp.getGoalTitle() + "\n" + temp.getGoalDueDate() + "\n" + temp.getGoalDescrip() + "\n");
        //close buffered writer
        bw4.close();
    }
    public void addGoal(ActionEvent actionEvent) throws IOException {
        //current goal to add to list
        Goal temp = new Goal(getGoalTitle.getText(), getGoalDueDate.getText(), getGoalDescrip.getText());
        //open goalInfo file to append to
        FileWriter fw4 = new FileWriter("goalInfo.txt", true);
        //write to file
        BufferedWriter bw4 = new BufferedWriter(fw4);
        //write goal title, due date, and description on 3 different lines
        bw4.write(getGoalTitle.getText() + "\n" + getGoalDueDate.getText() + "\n" + getGoalDescrip.getText() + "\n" );
        //close buffered writer
        bw4.close();
        //add to goal list
        goalList.getItems().add(temp);
        //clear goal title, due date, and description text field
        getGoalTitle.clear();
        getGoalDueDate.clear();
        getGoalDescrip.clear();
    }
    public void deleteGoal(ActionEvent actionEvent) {
        //remove selected goal from goal list
        goalList.getItems().remove(goalList.getSelectionModel().getSelectedItem());
        //clear goal title, due date, and description label
        lblGoalTitle.setText("Goal Title:");
        lblGoalDueDate.setText("Due Date:");
        lblGoalDescrip.setText("Description:");
    }
    public void displayGoal(MouseEvent mouseEvent) {
        //get currently selected goal from list
        Goal temp;
        temp = goalList.getSelectionModel().getSelectedItem();
        //set and display goal title, due date, and description label
        lblGoalTitle.setText("Goal Title: " + temp.getGoalTitle());
        lblGoalDueDate.setText("Due Date: " + temp.getGoalDueDate());
        lblGoalDescrip.setText("Description: " + temp.getGoalDescrip());
    }
}
