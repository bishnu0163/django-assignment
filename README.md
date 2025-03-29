# django-assignment
Here’s a properly structured description with explanations and examples based on your provided code. You can use this in your README file.  

---

## **Understanding Django Signals and Their Behavior**

Django signals provide a way to allow certain senders to notify other parts of the application when an action occurs. By default, Django signals are executed **synchronously**, run in the **same thread**, and are part of the **same database transaction** as the caller.


### **1. Are Django Signals Executed Synchronously by Default?**  

Yes, Django signals execute synchronously by default, meaning they block the main execution flow until they complete.  

The  example demonstrated in signal_sync.py shows that Django signals are synchronous:  

#### **Expected Output:**  
```
Before save
Signal started
Signal finished
After save
```

#### **Explanation:**  
- The message **"After save"** appears **only after** the signal completes execution.  
- Since the signal includes a `time.sleep(2)`, it delays the process by 2 seconds, proving that it runs **synchronously** and blocks the main thread.  

---

### **2. Do Django Signals Run in the Same Thread as the Caller?**  

Yes, Django signals run in the **same thread** as the caller, meaning they do not create a separate thread by default.  
As Shown in Example (signal_thread.py)
#### **Expected Output:**  
```
Main thread: MainThread
Signal thread: MainThread
```

#### **Explanation:**  
- The output shows that both the **main execution** and the **signal handler** run in the **same thread** (`MainThread`).  
- This behavior ensures that the signal does not introduce concurrency issues by default.  

---

### **3. Do Django Signals Run Within the Same Database Transaction as the Caller?**  

Yes, Django signals execute **within the same database transaction** as the caller. If the transaction is rolled back, any database changes made inside the signal are also rolled back.  

#### **Example:**  
We raise an exception inside the signal after modifying a model instance to check if the changes persist in folder(signal_transaction.py).  

#### **Expected Output:**  
```
Before commit: original
After rollback: original
```

#### **Explanation:**  
- The signal modifies the `name` field from `"original"` to `"modified"`.  
- However, since an **exception** is raised inside the signal, Django **rolls back the transaction**, and the model instance remains unchanged (`"original"`).  
- This confirms that the signal's database operations are part of the **same transaction** as the caller.  

---

## **Rectangle Class Implementation**  

This class represents a `Rectangle` with attributes `length` and `width`. It is designed to be **iterable**, meaning we can loop through its dimensions one by one.  

As Shown in example(signal_rectangle.py)
#### **Expected Output:**  
```
{'length': 5}
{'width': 3}
```

#### **Explanation:**  
- The `Rectangle` class has attributes `length` and `width`.  
- It implements the **`__iter__` method**, making it **iterable**.  
- When iterated over, it **yields** dictionaries, first returning the `length`, then the `width`.  
- This allows us to **loop through** the object and retrieve its dimensions in a structured format.  

---

