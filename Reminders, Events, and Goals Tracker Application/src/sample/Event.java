/*
This class contains information of the event such as the events title,
location, date, and description
The construction creates the event
You are able to print the events title
 */
package sample;

public class Event {
    private String eventTitle; //events title
    private String eventLocation; //events location
    private String eventDate; //events date
    private String eventDescrip; //events description

    //event constructor, it constructs the event
    public Event(String eventTitle, String eventLocation, String eventDate, String eventDescrip){
        this.eventTitle = eventTitle;
        this.eventLocation = eventLocation;
        this.eventDate = eventDate;
        this.eventDescrip = eventDescrip;
    }

    //returns the event's title
    @Override
    public String toString(){
        return eventTitle;
    }

    //getters and setters
    public String getEventTitle() {
        return eventTitle;
    }

    public void setEventTitle(String eventTitle) {
        this.eventTitle = eventTitle;
    }

    public String getEventLocation() {
        return eventLocation;
    }

    public void setEventLocation(String eventLocation) {
        this.eventLocation = eventLocation;
    }

    public String getEventDate() {
        return eventDate;
    }

    public void setEventDate(String eventDate) {
        this.eventDate = eventDate;
    }

    public String getEventDescription() {
        return eventDescrip;
    }

    public void setEventDescription(String eventDescription) {
        this.eventDescrip = eventDescription;
    }
}
