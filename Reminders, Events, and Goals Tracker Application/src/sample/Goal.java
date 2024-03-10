/*
This class contains information of the goal such as the goals title,
due date, and description
The construction creates the goal
You are able to print the goals title
 */
package sample;

public class Goal {
    private String goalTitle; //goal title
    private String goalDueDate; //goal due date
    private String goalDescrip; //goal description

    //goal constructor, it constructs the goal
    public Goal(String goalTitle, String goalDueDate, String goalDescrip){
        this.goalTitle = goalTitle;
        this.goalDueDate = goalDueDate;
        this.goalDescrip = goalDescrip;
    }

    //returns the goal's title
    @Override
    public String toString(){
        return goalTitle;
    }

    //getters and setters
    public String getGoalTitle() {
        return goalTitle;
    }

    public void setGoalTitle(String goalTitle) {
        this.goalTitle = goalTitle;
    }

    public String getGoalDueDate() {
        return goalDueDate;
    }

    public void setGoalDueDate(String goalDueDate) {
        this.goalDueDate = goalDueDate;
    }

    public String getGoalDescrip() {
        return goalDescrip;
    }

    public void setGoalDescrip(String goalDescrip) {
        this.goalDescrip = goalDescrip;
    }
}
