package exam_prep;

import java.util.ArrayList;

public class LabSession {
    // TODO: Define fields
    // - An ArrayList to hold the users (Hint: Use the Interface type, not specific classes!)
    // - An integer for the maximum capacity of the lab

    public LabSession(int capacity) {
        // TODO: Initialize the ArrayList and set the capacity
    }

    // TODO: Implement enterLab(LabAccess user)
    // Method signature should declare that it throws LabCapacityException
    // Logic:
    // 1. Check if the lab is already full (current size >= capacity). If so, throw the exception.
    // 2. Check if the user.canLogin(). 
    //    - If yes, add them to the list.
    //    - If no, print "Access Denied".
    
    
    // TODO: Implement viewUserList()
    // Logic:
    // 1. Loop through the list of active users.
    // 2. Print their details. 
    // Hint: You might need to check if the user is also a UniversityMember to get their role (instanceof check)
    //       or just print what you can from LabAccess.
}
