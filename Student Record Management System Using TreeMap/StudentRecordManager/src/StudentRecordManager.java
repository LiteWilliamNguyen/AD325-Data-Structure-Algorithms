import java.util.Map;
import java.util.TreeMap;

public class StudentRecordManager {
    private TreeMap<Integer, Student> studentRecords = new TreeMap<>();

    //Add a student record
    public boolean addStudent(int id, String name, double gpa){
        if (studentRecords.containsKey(id)){
            System.out.println("Student ID existed");
            return false;
        }
        studentRecords.put(id, new Student(id,name,gpa));
        System.out.println("Student have been added.");
        return true;
    }

    //Delete a student record

    public boolean deleteStudent(int id){
        if (studentRecords.remove(id) != null){
            System.out.println("Student have been removed.");
            return true;
        }
        System.out.println("Student ID not found");
        return false;
    }

    //Update Student GPA by given ID
    public boolean updateStudentGpa(int id, double newGpa){
        Student student = studentRecords.get(id);
        if (student!= null){
            student.setGpa(newGpa);
            return true;
        }
        System.out.println("Student ID not found");
        return false;
    }

    //Display all record
    public void displayAllRecord(){
        if (studentRecords.isEmpty()){
            System.out.println("No student in record");
        }
        else {
            for (Map.Entry<Integer,Student> entry: studentRecords.entrySet()){
                System.out.println(entry.getValue());
            }
        }
    }

    //Find Students with GPA Higher Than a Specified Value:
    public void findStudentHigherThanSpecifiedValue(double threshold){
        boolean found = false;

        for (Student student : studentRecords.values()){
            if (student.getGpa() > threshold){
                System.out.println(student);
                found = true;
            }
        }
        if(!found){
            System.out.println("No student is above the GPA value " + threshold);
        }

    }


}
