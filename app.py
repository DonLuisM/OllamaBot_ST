from ollama import chat
from ollama import ChatResponse
import streamlit as st
import time

st.title("Ollama Chatbot")
st.write("Este es un chatbot sencillo usando Ollama y Streamlit.")
st.write("Escribe algo y obten la respuesta del modelo!")

try: 
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Preguntame algo! 🤖"}]
except Exception as e:
    st.error(f"Error inicializando el modelo en streamlit: {e}")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if 'model_selection' not in st.session_state:
    st.session_state.model_selection = 'llama3.1'
    
with st.sidebar:
        st.session_state.model_selection = st.selectbox(
            'Select Model', 
            ['llama3.1', 'llama3.2', 'qwen2.5:3b', 'gemma3'],
            index=0
        )
        st.session_state.temperature = st.slider(
            'Temperature',
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.1
        )
        st.session_state.top_p = st.slider(
            'Top P',
            min_value=0.0,
            max_value=1.0,
            value=0.9,
            step=0.1
        )
        st.session_state.top_k = st.slider(
            'Top K',
            min_value=0,
            max_value=100,
            value=50,
            step=1
        )
        st.session_state.tokens = st.slider(
            'Max Tokens',
            min_value=1,
            max_value=4096,
            value=256,
            step=1
        )
        
try: 
    if user_input := st.chat_input('Realiza Pregunta'):
        with st.chat_message("user"):
            st.markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        with st.spinner("_Modelo generando respuesta..._"):
            responseFull: ChatResponse = chat(model=st.session_state.model_selection, messages=st.session_state.messages)
            response = responseFull['message']['content']
            combined_response = f'{response}\n\n**Respuesta Cruda:**\n{responseFull}'

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                
                for chunk in response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
            
        st.write("**Respuesta Cruda:**")
        with st.expander("Ver respuesta cruda"):
            st.write(responseFull)
        st.session_state.messages.append({"role": "assistant", "content": response})
        
except Exception as e:
    st.error(f"Error con el input o respuesta del modelo: {e}")
        
# or access fields directly from the response object
# st.write(response.message.content)