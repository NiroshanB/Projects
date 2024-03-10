import org.junit.Before;
import org.junit.Test;
import sample.Event;
import sample.Goal;
import sample.Reminder;

import static org.junit.Assert.assertEquals;

public class ControllerTest {
    //testing for reminder, event, and goal class methods

    private Event event;
    private Goal goal;
    private Reminder reminder;

    @Before
    public void initializeSetup() {
        reminder = new Reminder("Pay phone bill", "Feb 28, 2021", "Pay $60 telus phone bill at Metrotown before the end of the month");
        event = new Event("PNE", "Vancouver", "Feb 25, 2021", "Go to the PNE on Hastings street at 4pm with Alex and Ryan to setup carnival event.");
        goal = new Goal("Read 'The Giver'", "March 20, 2021", "Read 15 pages each day.");
    }

    //reminder test
    @Test
    public void testReminder() {
        //test reminder getters
        assertEquals("Pay phone bill", reminder.getReminderTitle());
        assertEquals("Feb 28, 2021", reminder.getReminderDueDate());
        assertEquals("Pay $60 telus phone bill at Metrotown before the end of the month", reminder.getReminderDescrip());
        //set new information
        reminder.setReminderTitle("Meeting with Ryan");
        reminder.setReminderDueDate("March 5, 2021");
        reminder.setReminderDescrip("Call Ryan at 8am and discuss work meeting about marketing.");
        //test reminders setters
        assertEquals("Meeting with Ryan", reminder.getReminderTitle());
        assertEquals("March 5, 2021", reminder.getReminderDueDate());
        assertEquals("Call Ryan at 8am and discuss work meeting about marketing.", reminder.getReminderDescrip());
    }

    //event test
    @Test
    public void testEvent() {
        //test event getters
        assertEquals("PNE", event.getEventTitle());
        assertEquals("Vancouver", event.getEventLocation());
        assertEquals("Feb 25, 2021", event.getEventDate());
        assertEquals("Go to the PNE on Hastings street at 4pm with Alex and Ryan to setup carnival event.", event.getEventDescription());
        //set new information
        event.setEventTitle("Alex's Birthday Party");
        event.setEventLocation("Hillcrest Community Centre");
        event.setEventDate("Feb 27, 2021");
        event.setEventDescription("Alex's 25th Birthday Party at 2pm.");
        //test event setters
        assertEquals("Alex's Birthday Party", event.getEventTitle());
        assertEquals("Hillcrest Community Centre", event.getEventLocation());
        assertEquals("Feb 27, 2021", event.getEventDate());
        assertEquals("Alex's 25th Birthday Party at 2pm.", event.getEventDescription());
    }

    //goal test
    @Test
    public void goalReminder(){
        //test goal getters
        assertEquals("Read 'The Giver'", goal.getGoalTitle());
        assertEquals("March 20, 2021", goal.getGoalDueDate());
        assertEquals("Read 15 pages each day.", goal.getGoalDescrip());
        //set new information
        goal.setGoalTitle("Do 100 pushups everday");
        goal.setGoalDueDate("March 23, 2021");
        goal.setGoalDescrip("Do 100 pushups everday for one month. Do 50 inclined pushups when you wake up and do 50 declined pushups before you go to sleep.");
        //tests goals setters
        assertEquals("Do 100 pushups everday", goal.getGoalTitle());
        assertEquals("March 23, 2021", goal.getGoalDueDate());
        assertEquals("Do 100 pushups everday for one month. Do 50 inclined pushups when you wake up and do 50 declined pushups before you go to sleep.", goal.getGoalDescrip());
    }
}
