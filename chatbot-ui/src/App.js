import React, { useState } from "react";
import "./App.css";

function App() {

  const [startChat, setStartChat] = useState(false);
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([
    {
      sender: "bot",
      text: "Hey hi, please tell me which quotes you want today (Inspirational/Motivational/Success/Love/Funny)"
    }
  ]);

  const sendMessage = async () => {

    if (message.trim() === "") return;

    const userMsg = { sender: "user", text: message };

    setChat([...chat, userMsg]);

    const response = await fetch("http://localhost:5005/webhooks/rest/webhook",{
      method:"POST",
      headers:{
        "Content-Type":"application/json"
      },
      body:JSON.stringify({
        sender:"user",
        message:message
      })
    });

    const data = await response.json();

    if(data.length > 0){
      const botMsg = {
        sender:"bot",
        text:data[0].text
      };

      setChat(prev => [...prev, botMsg]);
    }

    setMessage("");
  };


  return (

    <div className="app-container">

      {!startChat ? (

        <div className="landing-card">

          <h1>Daily Inspiration</h1>

          <p>
            Your personal AI companion for wisdom, motivation and clarity.
            Discover the perfect quote for every moment of your life.
          </p>

          <button onClick={() => setStartChat(true)}>
            START CHATTING
          </button>

          <div className="categories">
            <span>✨ Motivation</span>
            <span>❤️ Love</span>
            <span>🏆 Success</span>
          </div>

        </div>

      ) : (

        <div className="chat-container">

          <h2>Quotes Bot</h2>

          <div className="chat-box">

            {chat.map((msg,index)=>(
              <div key={index} className={msg.sender === "user" ? "user-msg" : "bot-msg"}>
                {msg.text}
              </div>
            ))}

          </div>

          <div className="input-area">

            <input
              type="text"
              placeholder="Type a message..."
              value={message}
              onChange={(e)=>setMessage(e.target.value)}
            />

            <button onClick={sendMessage}>
              Send
            </button>

          </div>

        </div>

      )}

    </div>

  );
}

export default App;