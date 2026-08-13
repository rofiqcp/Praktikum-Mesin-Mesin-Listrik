from trafo_no_load import transformer_ratio_sweep

if __name__ == "__main__":
    print("V1,V2_ideal,V2_model,I0_model,ratio_model")
    for r in transformer_ratio_sweep():
        print(f"{r[0]:.1f},{r[1]:.3f},{r[2]:.3f},{r[3]:.3f},{r[4]:.3f}")
