from flask import Flask, request, jsonify, render_template
from automata.fa.nfa import NFA
from automata.fa.dfa import DFA
import json

app = Flask(__name__)
def nfa_to_dfa(nfa_definition):
    try:
        nfa = NFA(
            states=set(nfa_definition["states"]),
            input_symbols=set(nfa_definition["input_symbols"]),
            transitions=nfa_definition["transitions"],
            initial_state=nfa_definition["initial_state"],
            final_states=set(nfa_definition["final_states"])
        )
        dfa = DFA.from_nfa(nfa)
        dfa_dict = {
            "states": list(dfa.states),
            "input_symbols": list(dfa.input_symbols),
            "transitions": {state: dict(transitions) for state, transitions in dfa.transitions.items()},
            "initial_state": dfa.initial_state,
            "final_states": list(dfa.final_states),
        }
        return dfa_dict
    except Exception as e:
        return {"error": str(e)}

def minimize_dfa(dfa_definition):
    try:
        dfa = DFA(
            states=set(dfa_definition["states"]),
            input_symbols=set(dfa_definition["input_symbols"]),
            transitions={state: {symbol: target for symbol, target in transitions.items()} for state, transitions in dfa_definition["transitions"].items()},
            initial_state=dfa_definition["initial_state"],
            final_states=set(dfa_definition["final_states"])
        )
        minimized_dfa = dfa.minify()
        minimized_dfa_dict = {
            "states": list(minimized_dfa.states),
            "input_symbols": list(minimized_dfa.input_symbols),
            "transitions": {state: dict(transitions) for state, transitions in minimized_dfa.transitions.items()},
            "initial_state": minimized_dfa.initial_state,
            "final_states": list(minimized_dfa.final_states),
        }
        return minimized_dfa_dict
    except Exception as e:
        return {"error": str(e)}

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/convert', methods=['POST'])
def convert():
    try:
        data = request.get_json()
        nfa_definition = data.get('nfa')
        if not nfa_definition:
            return jsonify({"error": "NFA definition not provided."}), 400
        
        dfa = nfa_to_dfa(nfa_definition)
        if "error" in dfa:
            return jsonify({"error": dfa["error"]}), 400
        return jsonify({"dfa": dfa})
    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True )
