/*
This class contains information of the reminder such as the reminders title,
due date, and description
The construction creates the reminder
You are able to print the reminders title
 */
package sample;

public class Reminder {
    private String reminderTitle; //reminder title
    private String reminderDueDate; //reminder due date
    private String reminderDescrip; //reminder description

    //reminder constructor, it constructs the reminder
    public Reminder(String reminderTitle, String reminderDueDate, String reminderDescrip){
        this.reminderTitle = reminderTitle;
        this.reminderDueDate = reminderDueDate;
        this.reminderDescrip = reminderDescrip;
    }

    //returns the reminder's title
    @Override
    public String toString(){
        return reminderTitle;
    }

    //getters and setters
    public String getReminderTitle() {
        return reminderTitle;
    }

    public void setReminderTitle(String reminderTitle) {
        this.reminderTitle = reminderTitle;
    }

    public String getReminderDueDate() {
        return reminderDueDate;
    }

    public void setReminderDueDate(String reminderDueDate) {
        this.reminderDueDate = reminderDueDate;
    }

    public String getReminderDescrip() {
        return reminderDescrip;
    }

    public void setReminderDescrip(String reminderDescrip) {
        this.reminderDescrip = reminderDescrip;
    }
}
