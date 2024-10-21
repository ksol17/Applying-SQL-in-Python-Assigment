from connect_mysql import connect_database

# Function to add a new member 
def add_member(cursor, member_id, name, age):
    """
    Adds a new member to the Members table
    """
    try:
        query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
        cursor.execute(query, (member_id, name, age))
        print(f"Member {name} added successfully.")
    except Exception as e:
        print(f"Error adding member: {e}")


# Function to add a workout session
def add_workout_session(cursor, session_id, member_id, session_date, session_time, activity):
    """
    Adds a new workout session to the WorkoutSessions table.
    """
    try:
        query = """
        INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) 
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (session_id, member_id, session_date, session_time, activity))
        print(f"Workout session for member {member_id} added successfully.")
    except Exception as e:
        print(f"Error adding workout session: {e}")


# Function to update a member's age
def update_member_age(cursor, member_id, new_age):
    """
    Updates the age of a member.
    Checks if the member exists before updating.
    """
    try:
        # Check if the member exists
        check_query = "SELECT COUNT(*) FROM Members WHERE id = %s"
        cursor.execute(check_query, (new_age, member_id))
        member_exists = cursor.fetchone()[0]

        if member_exists:
            update_query = "UPDATE Members SET age = %s WHERE id = %s"
            cursor.execute(update_query, (new_age, member_id))
            print(f"Member with ID {member_id}'s age updated to {new_age}")
        else:
            print(f"Error: Member with ID {member_id} does not exist.")
    except Exception as e:
        print(f"Error: Member with ID {member_id} does not exist.")


# Function to delete a workout session by session ID
def delete_workout_session(cursor, session_id):
    """
    Deletes a workout session by session ID.
    Handles cases where the session ID does not exist.
    """
    try:
        # Check if the session exists.
        check_query = "SELECT COUNT(*) FROM WorkoutSessions WHERE session_id = %s"
        cursor.execute(check_query, (session_id))
        session_exists = cursor.fetchone()[0]

        if session_exists:
            delete_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(delete_query, (session_id,))
            print(f"Workout sesssion with ID {session_id} deleted successfully.")
        else:
            print(f"Error: Workout session with ID {session_id} does not exist.")
    except Exception as e:
        print(f"Error deleting workout session: {e}")


def get_members_in_age_range(cursor, start_age, end_age):
    """
    Retrieves details of members whose ages are between start_age and end_age.
    """
    try:
        # SQL query using BETWEEN
        query = "SELECT id, name, age FROM Members WHERE age BETWEEN %s AND %s"
        cursor.execute(query, (start_age, end_age))

        # Fetch all the matching records
        members = cursor.fetchall()

        # Check if any members are found
        if members:
            print(f"Members between ages {start_age} and {end_age}:")
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")
        else:
            print(f"No members found between ages {start_age} and {end_age}.")

    except Exception as e:
        print(f"Error retrieving members: {e}")


# Main function to handle database operations
def main(): 
    conn = connect_database()

    if conn is not None: 
        try:
            cursor = conn.cursor()

            # Add a new member (make sure id and age are integers)
            add_member(cursor, 1, "Snow White", 19)

            # Add workout session (Example: sessio_id 9, for member 2)
            add_workout_session(cursor, 10, 2, "2024-10-20", "5:15 AM", "Cardio")

            # Update a member's age (Example: ID: 1, new age 26)
            update_member_age(cursor, 5, 26)

            # Delete a workout session (Example: session_id 1)
            delete_workout_session(cursor, 3)

            # Get members between ages 25 and 30
            get_members_in_age_range(cursor, 25, 30)

            # Commit the transaction to the database
            conn.commit()
    

        except Exception as e:
            # Handle any exceptions during database operations
            print(f"Error: {e}")

        finally:
            # Close the cursor and connection to avoid resource leaks
            cursor.close()
            conn.close()

# Run the main function
if __name__ == "__main__":
    main()
