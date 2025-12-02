package exam_prep;

public class ExamRunner {
    public static void main(String[] args){
     Student student = new Student("123456789","John",2.2);
     TeachingAssistant ta = new TeachingAssistant("123987456", "Bill", 6.2);
    Professor professor = new Professor("987654321","Goggins","Mathematics");
        // 1. Create the array
    UniversityMember[] members = { student, professor, ta}; 

    // 2. Loop over the ARRAY (members)
    for (UniversityMember m : members) {
        // System.out.println(m.getRole()); 
        if (m instanceof LabAccess) {
            System.out.println(((LabAccess) m).getPrintQuota()); 
        }
    } 
    // Student student2 = new Student("123456789","Greg",2.2);
    // System.out.println(student.equals(student2));
    
    // --- Phase 3: Lab Session & Exceptions ---
    // TODO: 1. Create a LabSession with a capacity of 2
    // TODO: 2. Wrap the following in a try-catch block for LabCapacityException:
    //          - Try to enter the student
    //          - Try to enter the professor
    //          - Try to enter the TA (This should throw the exception if capacity is 2)
    // TODO: 3. Call viewUserList() to see who made it in

    }
}
