import BP_classes as bpc
import BP_graphs as bpg
import BP_gui as bp_gui
import File_Handling_functions as fh
import BP_functions as bpf


def main():

    Coordinates = fh.read_file("bola.txt")

    Robot = bpf.create_robot()
    Ball = bpf.create_ball()
    Field = bpf.create_field(Ball, Robot, Coordinates)

    Field.run_coordinates()

    bpf.get_interception_points(Field)

    Graph = bpg.Equation(Field)

    # Graph.plot_graph_one()
    # Graph.plot_graph_three()
    # Graph.plot_graph_four()


if __name__ == "__main__":
    main()
