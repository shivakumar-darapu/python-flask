function App() {

	return (
		<div className="App">
				<>
					<TodoList />
				</>

			<Foobar />
		</div>
	);
}

function TodoList() {
	const generateID = () => {
		let result = "";
		let input_length = 5;
		let chars =
			"[@678^#(ABC,F3qr.sIJKN_+}{:OPQRghi)jDEklm:~noGH=2pL*$Mtuvwx<STU1>5VW`XYZa4bcd&efyz09]";
		for (var i = 0; i < input_length; i++) {
			result += chars.charAt(Math.floor(Math.random() * chars.length));
		}
		return result;
	};
	const sortList = (a, b) => {
		return a.isCompleted > b.isCompleted
			? 1
			: b.isCompleted > a.isCompleted
			? -1
			: 0;
	};
	const [todoList, setTodoList] = React.useState(
		[
			{ id: 1, taskName: "dummy text", isCompleted: false },
			{ id: 2, taskName: "dummy text", isCompleted: false },
			{ id: 3, taskName: "dummy text", isCompleted: true },
			{ id: 4, taskName: "dummy text", isCompleted: false },
			{ id: 5, taskName: "dummy text", isCompleted: false },
			{ id: 6, taskName: "dummy text", isCompleted: false },
		].sort(sortList)
	);
	const [newTask, setNewTask] = React.useState("");

	const inputRef = React.useRef(null);
	const btnRef = React.useRef(null);

	const handleChange = (e) => {
		e.preventDefault();
		setNewTask(e.target.value);
		console.log(newTask);
	};
	React.useEffect(() => {
		const listener = (event) => {
			if (event.code === "Enter" || event.code === "NumpadEnter") {
				btnRef.current.click();
			}
		};
		inputRef.current.addEventListener("keydown", listener);
		return () => {
			inputRef.current.removeEventListener("keydown", listener);
		};
	}, []);

	const handleDelete = (id) => {
		setTodoList(todoList.filter((list) => list.id !== id));
	};

	const handleEdit = (content) => {
		setNewTask(content.taskName);
		inputRef.current.value = content.taskName;
		inputRef.current.focus();

		setTodoList(todoList.filter((list) => list.id !== content.id));
	};
	const handleDone = (status) => {
		status.isCompleted = true;
		setTodoList([...todoList.sort(sortList)]);
	};
	const addTask = () => {
		if (inputRef.current.value !== "") {
			const task = {
				id: todoList.length === 0 ? 1 : generateID(),
				taskName: newTask,
				isCompleted: false,
			};
			setTodoList([...todoList, task].sort(sortList));
			setNewTask("");
			inputRef.current.value = "";
			inputRef.current.focus();
		} else {
			alert(customeAlert());
		}
	};
	const customeAlert = () => {
		let alertMsgs = [
			"Please type in something",
			"input can't be empty",
			"Invalid input",
			"something went wrong",
		];
		let msgIndex = Math.floor(Math.random() * alertMsgs.length);
		let randomMsg = alertMsgs[msgIndex];

		return randomMsg;
	};

	return (
		<div className="todolist">
			<div className="title">
				<h1>TODO APP</h1>
			</div>

			<div className="addTask">
				<input
					ref={inputRef}
					type="text"
					onChange={handleChange}
					placeholder="Add a task........"
				/>
				<button ref={btnRef} onClick={addTask} className='addtask-btn'>
					Add Task
				</button>
			</div>
			<div className="lists">
				{todoList.length > 0 ? (
					<>
						{todoList.map((list, id) => (
							<div
								key={id}
								className={`list ${list.isCompleted ? "completed" : ""}`}
							>
								<p> {list.taskName}</p>
								<div className="span-btns">
									<span
										style={{ opacity: list.isCompleted ? "0" : "1" }}
										onClick={() => handleDone(list)}
										title="completed"
									>
										✓
									</span>
									<span
										className="delete-btn"
										onClick={() => handleDelete(list.id)}
										title="delete"
									>
										X
									</span>
									<span
										className="edit-btn"
										onClick={() => handleEdit(list)}
										title="edit"
									>
										↻
									</span>
								</div>
							</div>
						))}
					</>
				) : (
					<h1>Nothing To see here</h1>
				)}
			</div>
		</div>
	);
}


const Foobar = () => {
	return (
		<div id="foobar">Made with 💙 Liquid | {new Date().getFullYear()}</div>
	);
};
// Tells React to attach the HelloWorld component to the 'root' HTML div
ReactDOM.render(<App />, document.getElementById("root"))
